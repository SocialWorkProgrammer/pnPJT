import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인페이지
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      // 게시판
      path: '/community',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      // 게시판 폼 페이지
      path: '/community',
      name: 'CreateArticleView',
      component: CreateArticleView
    },
    {
      // 게시판 상세페이지
      path: '/community/article/:id/',
      name: 'DetailView',
      component: DetailView
    },
    {
      // 로그인 폼
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      // 가입 폼
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },

  ]
})

import { useBoardStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useBoardStore()
  if (to.name === 'Articleview' && store.isLogin === false) {
    window.alert('로긴 해라')
    return { name : 'LoginView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LoginView') && (store.isLogin))
  {window.alert('뭣')
  return { name: 'ArticleView'}
}
})

export default router
