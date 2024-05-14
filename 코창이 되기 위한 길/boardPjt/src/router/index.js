import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/community',
      name: 'CreateArticleView',
      component: CreateArticleView
    },
    {
      path: '/article/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
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
