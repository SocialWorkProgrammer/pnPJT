import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView/HomeView.vue'
import ArticleView from '@/views/ArticleView/ArticleView.vue'
import CreateArticleView from '@/views/ArticleView/CreateArticleView.vue'
import DetailView from '@/views/ArticleView/DetailView.vue'
import LoginView from '@/views/HomeView/LoginView.vue'
import SignUpView from '@/views/HomeView/SignUpView.vue'
import MapView from '@/views/FunctionView/MapView.vue'
import ExchangeView from '@/views/FunctionView/ExchangeView.vue'
import MainView from '@/views/HomeView/MainView.vue'
import ArticleUpdate from '@/components/articles/ArticleUpdate.vue'
import CommentUpdate from '@/components/comments/CommentUpdate.vue'
import DepositView from '@/views/FinanceView/DepositView.vue'
import SavingView from '@/views/FinanceView/SavingView.vue'
import DepositDetailView from '@/views/FinanceView/DepositDetailView.vue'
import SavingDetailView from '@/views/FinanceView/SavingDetailView.vue'
import ProfileView from '@/views/HomeView/ProfileView.vue'
import ProfileDetailView from '@/views/HomeView/ProfileDetailView.vue'
import ProfileSignUpView from '@/views/HomeView/ProfileSignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인페이지
      path: '/',
      children: [
        // {path: '', name: 'HomeView', component: HomeView},
        {path: 'login/', name: 'LoginView', component: LoginView},
        {path: 'signup/', name: 'SignUpView', component: SignUpView},
        {path: 'exchange/', name: 'ExchangeView', component: ExchangeView},
        {path: '', name: 'MainView', component: MainView},
        {path: 'profile/:username/', name: 'ProfileView', component: ProfileView},
        {path: 'profile/:username/detail', name: 'ProfileDetailView', component: ProfileDetailView},
        {path: 'profile/:username/finance', name: 'ProfileSignUpView', component: ProfileSignUpView},
      ]
    },
    {
      // 게시판
      path: '/community',
      children: [
        {path: '', name: 'ArticleView', component: ArticleView},
        {path : 'create/', name: "CreateArticleView", component: CreateArticleView},
        {path : 'article/:id/', name: "DetailView", component: DetailView},
        {path : 'article/:id/', name: "ArticleUpdate", component: ArticleUpdate},
        {path : 'article/:id/comment/:commentId', name: "CommentUpdate", component: CommentUpdate},
      ]
    },
    {
      // 지도
      path: '/map',
      children: [
        {path: '', name: 'MapView', component: MapView},
      ]
    },
    {
      // 금융
      path: '/finance',
      children: [
        {path: '', name: 'DepositView', component: DepositView},
        {path: 'saving', name: 'SavingView', component: SavingView},
        {path: ':id/', name:'DepositDetailView', component: DepositDetailView},
        {path: 'saving/:id', name:'SavingDetailView', component: SavingDetailView},
      ]
    },
  ]
})

import { useBoardStore } from '@/stores/counter'

router.beforeEach((to, from, next) => {
  const store = useBoardStore()
  
  if (to.name === 'MainView' && !store.isLogin) {
    window.alert('로그인해주세요')
    next({ name: 'LoginView' })
  } else if (to.name === 'LoginView' && store.isLogin) {
    window.alert('이미 로그인이 된 상태입니다.')
    next({ name: 'MainView' })
  } else {
    next() // 통과
  }
})

export default router

// 로컬 스토리지 쪽에서는 null을 ""로 저장한다. 
// 이유 : 로컬 스토리지는 문자열로 저장하기 때문에, null값을 " null "로 인식해서 빈 문자열로 저장하기 때문
// 그렇기 때문에 원래는 return token !== null으로 썼었는데,
// 실제 할 때는 return token !== ""으로 써야 한다.
// 아니면 아래 코드처럼 삼항식을 이용해 lenght가 0 이상이면 true(로그인 되어있는 상태), 아니면 false(로그인이 되어있지 않은 상태)
// 로 인식시키면 된다.
//const isLogin = computed(() => {
//  return token.value.length > 0 ? true : false
//  return token !== null
//  })
