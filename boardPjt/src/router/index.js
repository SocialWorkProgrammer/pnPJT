import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView/HomeView.vue'
import ArticleView from '@/views/ArticleView/ArticleView.vue'
import CreateArticleView from '@/views/ArticleView/CreateArticleView.vue'
import DetailView from '@/views/ArticleView/DetailView.vue'
import LoginView from '@/views/HomeView/LoginView.vue'
import SignUpView from '@/views/HomeView/SignUpView.vue'
import MapView from '@/views/FunctionView/MapView.vue'
import ExchangeView from '@/views/FunctionView/ExchangeView.vue'
import ArticleUpdate from '@/components/articles/ArticleUpdate.vue'
import CommentUpdate from '@/components/comments/CommentUpdate.vue'
import { useBoardStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인페이지
      path: '/',
      name: 'HomeView',
      component: HomeView,
      children: [
        { path: 'login', name: 'LoginView', component: LoginView },
        { path: 'signup', name: 'SignUpView', component: SignUpView },
        { path: 'exchange', name: 'ExchangeView', component: ExchangeView }
      ]
    },
    {
      // 게시판
      path: '/community',
      children: [
        { path: '', name: 'ArticleView', component: ArticleView },
        { path: 'create', name: 'CreateArticleView', component: CreateArticleView },
        { path: 'article/:id', name: 'DetailView', component: DetailView },
        { path: 'article/:id/update', name: 'ArticleUpdate', component: ArticleUpdate },
        { path: 'article/:id/comment/:commentId', name: 'CommentUpdate', component: CommentUpdate, props: true },
      ]
    },
    {
      // 지도
      path: '/map',
      name: 'MapView',
      component: MapView
    }
  ]
})

router.beforeEach((to, from, next) => {
  const store = useBoardStore()
  
  // 로그인 필수 페이지 체크
  const requiresAuth = ['ArticleView', 'CreateArticleView', 'DetailView', 'ArticleUpdate', 'CommentUpdate']
  if (requiresAuth.includes(to.name) && !store.isLogin) {
    window.alert('로그인해주세요')
    next({ name: 'LoginView' })
  } else if ((to.name === 'SignUpView' || to.name === 'LoginView') && store.isLogin) {
    window.alert('이미 로그인이 된 상태입니다.')
    next({ name: 'HomeView' })
  } else {
    next()
  }
})

export default router
