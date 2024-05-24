<template>
  <div class="container my-5">
    <h1>주변 은행 검색</h1>
    <div class="d-flex align-center my-5">
      <v-select
        :items="cities"
        label="광역시 / 도"
        v-model="selectedCity"
        class="mr-2"
      ></v-select>

      <v-select
        :items="citiesDetail"
        label="시/군/구"
        v-model="selectedCityDetail"
        class="mx-2"
      ></v-select>

      <v-select
        :items="banks"
        label="은행"
        v-model="selectedBank"
        class="mx-2"
      ></v-select>

      <v-btn @click="clickSearch" class="ml-2">찾기</v-btn>
    </div>
    <div class="map-container mb-15">
      <v-btn @click="clickCurrentSearch" class="current-search-btn">
        현 지도에서 해당 은행 검색
      </v-btn>
      <div id="map" class="map"></div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useBoardStore } from '@/stores/counter'
import axios from 'axios'

const store = useBoardStore()
const router = useRouter()

const selectedBank = ref('전체보기')
const banks = ref(['우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '국민은행', '신한은행', '농협은행', '하나은행', '수협은행'])

const selectedCity = ref('전체보기')
const cities = ref(['서울특별시', '인천시', '경기도', '강원도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '울산광역시', '전라남도', '전라북도', '제주특별자치도', '충청남도', '충청북도'])
const selectedCityDetail = ref('전체보기')
const citiesDetail = ref([])

const keyword = ref('은행')

const cityDetails = {
  "강원도": ["강릉시","동해시","삼척시","속초시","원주시","춘천시","태백시","고성군","양구군","양양군","영월군","인제군","정선군","철원군","평창군","홍천군","화천군","횡성군"],
  "경기도": ["고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시","가평군","양평군","여주군","연천군"],
  "경상남도": ["거제시", "김해시", "마산시", "밀양시", "사천시", "양산시", "진주시", "진해시", "창원시", "통영시", "거창군", "고성군", "남해군", "산청군", "의령군", "창녕군", "하동군", "함안군", "함양군", "합천군"],
  "경상북도": ["경산시","경주시","구미시","김천시","문경시","상주시","안동시","영주시","영천시","포항시","고령군","군위군","봉화군","성주군","영덕군","영양군","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군"],
  "광주광역시": ["광산구", "남구", "동구", "북구", "서구"],
  "대구광역시": ["남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군"],
  "대전광역시": ["대덕구", "동구", "서구", "유성구", "중구"],
  "부산광역시": ["강서구","금정구","남구","동구","동래구","부산진구","북구","사상구","사하구","서구","수영구","연제구","영도구","중구","해운대구","기장군"],
  "서울특별시": ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구","중구","중랑구"],
  "울산광역시": ["남구","동구","북구","중구","울주군"],
  "인천시": ["계양구","남구","남동구","동구","부평구","서구","연수구","중구","강화군","옹진군"],
  "전라남도": ["광양시","나주시","목포시","순천시","여수시","강진군","고흥군","곡성군","구례군","담양군","무안군","보성군","신안군","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"],
  "전라북도": ["군산시", "김제시", "남원시", "익산시", "전주시", "정읍시", "고창군", "무주군", "부안군", "순창군", "완주군", "임실군", "장수군", "진안군"],
  "제주특별자치도": ["서귀포시","제주시","남제주군","북제주군"],
  "충청남도": ["계룡시","공주시","논산시","당진시","보령시","서산시","아산시","천안시","금산군","부여군","서천군","연기군","예산군","청양군","태안군","홍성군"],
  "충청북도": ["제천시","청주시","충주시","괴산군","단양군","보은군","영동군","옥천군","음성군","증평군","진천군","청원군"]
}

watch(selectedCity, () => {
  selectedCityDetail.value = null
  citiesDetail.value = cityDetails[selectedCity.value] || []
})

watch([selectedCity, selectedCityDetail, selectedBank], () => {
  keyword.value = ''
  if (selectedCity.value) {
    keyword.value += `${selectedCity.value} `
  }
  if (selectedCityDetail.value) {
    keyword.value += `${selectedCityDetail.value} `
  }
  if (selectedBank.value) {
    if (selectedBank.value === '전체보기') {
      keyword.value += '은행'
    } else {
      keyword.value += `${selectedBank.value}`
    }
  }
})

const MAP_API_KEY = "5453b871a455506269e91eafc81b92c2"
const center = ref([37.566826, 126.9786567])
const level = ref(3)
const mapRef = ref(null)

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap()
  } else {
    const script = document.createElement('script')
    script.onload = () => kakao.maps.load(() => initMap())
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${MAP_API_KEY}&libraries=services`
    document.head.appendChild(script)
  }
})

const initMap = () => {
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
  const mapContainer = document.getElementById('map')
  const mapOption = {
    center: new kakao.maps.LatLng(center.value[0], center.value[1]),
    level: level.value
  }

  const map = new kakao.maps.Map(mapContainer, mapOption)
  mapRef.value = map

  map.addControl(new kakao.maps.ZoomControl(), kakao.maps.ControlPosition.RIGHT)

  const places = new kakao.maps.services.Places()
  const searchPlaces = () => {
    places.keywordSearch(keyword.value, (data, status, pagination) => {
      if (status === kakao.maps.services.Status.OK) {
        const bounds = new kakao.maps.LatLngBounds()
        data.forEach(item => {
          const marker = new kakao.maps.Marker({
            map,
            position: new kakao.maps.LatLng(item.y, item.x)
          })
          kakao.maps.event.addListener(marker, 'click', () => {
            infowindow.setContent(`
              <div style="padding:5px;font-size:12px;">
                ${item.place_name}<br>
                ${item.road_address_name || item.address_name}
              </div>
            `)
            infowindow.open(map, marker)
          })
          bounds.extend(new kakao.maps.LatLng(item.y, item.x))
        })
        map.setBounds(bounds)
      }
    })
  }
  
  searchPlaces()
}

const clickSearch = () => {
  initMap()
}

const clickCurrentSearch = () => {
  if (mapRef.value) {
    const bounds = mapRef.value.getBounds()
    const swLatLng = bounds.getSouthWest()
    const neLatLng = bounds.getNorthEast()
    const keywordSearchOptions = {
      bounds: new kakao.maps.LatLngBounds(
        new kakao.maps.LatLng(swLatLng.getLat(), swLatLng.getLng()),
        new kakao.maps.LatLng(neLatLng.getLat(), neLatLng.getLng())
      )
    }
    const places = new kakao.maps.services.Places()
    places.keywordSearch(keyword.value, (data, status, pagination) => {
      if (status === kakao.maps.services.Status.OK) {
        const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
        data.forEach(item => {
          const marker = new kakao.maps.Marker({
            map: mapRef.value,
            position: new kakao.maps.LatLng(item.y, item.x)
          })
          kakao.maps.event.addListener(marker, 'click', () => {
            infowindow.setContent(`
              <div style="padding:5px;font-size:12px;">
                ${item.place_name}<br>
                ${item.road_address_name || item.address_name}
              </div>
            `)
            infowindow.open(mapRef.value, marker)
          })
        })
      }
    }, keywordSearchOptions)
  }
}
</script>



<style scoped>

.map-container {
  position: relative;
}

.map {
  width: 100%;
  height: 500px;
}

.current-search-btn {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 2;
}
</style>
