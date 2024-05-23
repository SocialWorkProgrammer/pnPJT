  <template>
    <div class="exchange-form">
    <v-card class="elderly-friendly-card">
      <v-form>
        <v-container>
          <v-row>
            <v-col cols="3" offset="9">
              <v-select
                color="#1089FF"
                variant="outlined"
                :items="states"
                density="comfortable"
                label="기준"
                v-model="selectedState"
                class="elderly-friendly-select"
              ></v-select>
            </v-col>
          </v-row>
  
          <v-row no-gutter>
            <v-col cols="3">
              <v-select
                color="#1089FF"
                variant="outlined"
                label="통화 선택"
                :items="currencies"
                v-model="selectedCurrency"
                class="elderly-friendly-select"
              ></v-select>
            </v-col>
            <v-col cols="9">
              <v-text-field
                type="number"
                color="#1089FF"
                variant="outlined"
                :label="selectedCurrencyUnit"
                v-model="otherInput"
                @input="inputEventOther"
                class="elderly-friendly-input"
              ></v-text-field>
            </v-col>
          </v-row>
  
          <v-row class="my-0">
            <v-text-field
              type="number"
              append-inner-icon="mdi-currency-krw"
              color="#1089FF"
              variant="outlined"
              label="KRW"
              class="elderly-friendly-input mx-3"
              v-model="krwInput"
              @input="inputEventKrw"
            ></v-text-field>
          </v-row>
        </v-container>
      </v-form>    
    </v-card>
  </div>
  </template>


<script setup>
import { ref, onMounted, watch } from 'vue'
import { useBoardStore } from '@/stores/counter'
import axios from 'axios'

const currencies = ref()
const response = ref()
const selectedState = ref('송금 받으실 때')
const selectedCurrency = ref('미국 달러')
const selectedCurrencyUnit = ref('외화')
const selectedTtb = ref() // ttb: 송금 받으실 때
const selectedTts = ref() // tts: 송금 보내실 때
const selectedDeal = ref() // deal_bas_r : 매매 기준율

const calculateVariable = ref()
const krwInput = ref()
const otherInput = ref()

const states = ['송금 받으실 때', '송금 보내실 때', '매매 기준율']

const store = useBoardStore()

const emit = defineEmits(['passCurrency'])

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/exchange/`
  })
    .then((res) => {
      response.value = res.data.filter(data => data['ttb'] !== '0')
      currencies.value = response.value.map(item => item['cur_nm'])
      const units = response.value.map(item => item['cur_unit'])
      emit('passCurrency', currencies.value, units)
      const usdInfo = response.value.find(item => item['cur_nm'] === '미국 달러')
      selectedTtb.value = Number(usdInfo['ttb'].replaceAll(',', ''))
      selectedTts.value = Number(usdInfo['tts'].replaceAll(',', ''))
      selectedDeal.value = Number(usdInfo['deal_bas_r'].replaceAll(',', ''))
      calculateVariable.value = selectedTtb.value
    })
})

watch(selectedState, () => {
  if (selectedState.value === '송금 받으실 때') {
    calculateVariable.value = selectedTtb.value
  } else if (selectedState.value === '송금 보내실 때') {
    calculateVariable.value = selectedTts.value
  } else {
    calculateVariable.value = selectedDeal.value
  }
  inputEventOther()
})

const roundToTwo = (num) => {
  return +(Math.round(num + 'e+2') + 'e-2')
}

const inputEventKrw = function () {
  otherInput.value = krwInput.value / calculateVariable.value
  otherInput.value = roundToTwo(otherInput.value)
}

const inputEventOther = function () {
  krwInput.value = otherInput.value * calculateVariable.value
  krwInput.value = roundToTwo(krwInput.value)
}
</script>


<style scoped>
.exchange-form {
  background-color: white;
  margin : 10px;
  padding : 1rem;
}

.elderly-friendly-card {
  font-size: 1.25rem; /* 텍스트 크기 확대 */
  line-height: 1.75rem; /* 행 간격 확대 */
  padding: 2rem; /* 카드 내부 패딩 */
  border: 2px solid #ccc; /* 카드 테두리 */
  background-color: white; /* 배경색 */
}

.elderly-friendly-select, .elderly-friendly-input {
  font-size: 1.25rem; /* 입력 필드 및 선택 상자의 텍스트 크기 확대 */
  padding: 0.75rem; /* 입력 필드 및 선택 상자의 내부 패딩 확대 */
}

.elderly-friendly-input input {
  font-size: 1.25rem; /* 실제 입력 텍스트 크기 확대 */
}

.v-select__selections, .v-input__control {
  font-size: 1.25rem; /* 드롭다운 및 입력 컨트롤 텍스트 크기 확대 */
}

.elderly-friendly-input .v-text-field__append-inner-icon, .elderly-friendly-input .v-input__append-inner {
  font-size: 1.5rem; /* 아이콘 크기 확대 */
}

.elderly-friendly-input .v-input__append-inner-icon, .elderly-friendly-input .v-input__control {
  color: #1089FF; /* 아이콘 색상 */
}
</style>
