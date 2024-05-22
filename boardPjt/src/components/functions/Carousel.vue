<template>
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <ol class="carousel-indicators">
      <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"></li>
      <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></li>
      <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <a :href="slides[0].link">
          <img class="d-block w-100 carousel-img" :src="slides[0].image" :alt="slides[0].alt">
        </a>
      </div>
      <div class="carousel-item" v-for="(slide, index) in slides.slice(1)" :key="index">
        <a :href="slide.link">
          <img class="d-block w-100 carousel-img" :src="slide.image" :alt="slide.alt">
        </a>
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</template>

<script>
import voicePhishingImage from '@/assets/보이스피싱.png';
import jobSupportImage from '@/assets/취업지원센터.png';
import seniorEducationImage from '@/assets/시니어교육.jpg';

export default {
  data() {
    return {
      slides: [
        {
          image: voicePhishingImage,
          alt: '금융감독원 보이스피싱신고센터',
          link: 'https://fss.or.kr/fss/main/sub1voice.do?menuNo=200012'
        },
        {
          image: jobSupportImage,
          alt: '서울시어르신취업지원센터 온라인취업교육포털',
          link: 'https://lms.goldenjob.or.kr/main/main.asp'
        },
        {
          image: seniorEducationImage,
          alt: '어르신 금융교육',
          link: 'http://www.sfec.or.kr/HyAdmin/list.php?bbs_id=bo06'
        }
      ]
    };
  },
  mounted() {
    // Bootstrap Carousel 초기화
    const carouselElement = document.querySelector('#carouselExampleIndicators');
    new bootstrap.Carousel(carouselElement, {
      interval: 2000,
      wrap: true
    });
  }
};
</script>

<style>
.carousel-item img {
  max-height: 500px;
  object-fit: contain; /* 이미지를 축소하여 모든 내용이 표시되게 함 */
  width: auto; /* 비율을 유지하면서 이미지의 가로 크기를 자동으로 조정 */
  margin: auto; /* 이미지를 중앙에 배치 */
}
</style>
