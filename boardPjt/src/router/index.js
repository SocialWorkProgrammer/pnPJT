import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView/HomeView.vue'
import ArticleView from '@/views/ArticleView/ArticleView.vue'
import CreateArticleView from '@/views/ArticleView/CreateArticleView.vue'
import DetailView from '@/views/ArticleView/DetailView.vue'
import LoginView from '@/views/HomeView/LoginView.vue'
import SignUpView from '@/views/HomeView/SignUpView.vue'
import MapView from '@/views/FunctionView/MapView.vue'
import ExchangeView from '@/views/FunctionView/ExchangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인페이지
      path: '/',
      children: [
        {path: '', name: 'HomeView', component: HomeView},
        {path: 'login/', name: 'LoginView', component: LoginView},
        {path: 'signup/', name: 'SignUpView', component: SignUpView},
        {path: 'exchange/', name: 'ExchangeView', component: ExchangeView},
      ]
    },
    {
      // 게시판
      path: '/community',
      children: [
        {path: '', name: 'ArticleView', component: ArticleView},
        {path : 'create/', name: "CreateArticleView", component: CreateArticleView},
        {path : 'article/:id/', name: "DetailView", component: DetailView},
      ]
    },
    {
      // 지도
      path: '/map',
      children: [
        {path: '', name: 'MapView', component: MapView},
      ]
    },
  ]
})

// import { useBoardStore } from '@/stores/counter'

// router.beforeEach((to, from) => {
//   const store = useBoardStore()
//   if (to.name === 'Articleview' && store.isLogin === false) {
//     window.alert('로그인해주세요')
//     return { name : 'LoginView'}
//   }
//   if ((to.name === 'SignUpView' || to.name === 'LoginView') && (store.isLogin))
//   {window.alert('이미 로그인이 된 상태입니다.')
//   return { name: 'HomeView'}
// }
// })

export default router
