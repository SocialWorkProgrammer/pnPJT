import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import { useBoardStore } from '@/stores/counter'

// 부트스트랩 설치
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

// 뷰티파이 설치
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Vuetify 인스턴스 생성
const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
const pinia = createPinia()

// `createPersistedState` 사용하여 플러그인 등록
pinia.use(createPersistedState())

app.use(pinia)
app.use(router)
app.use(vuetify) // Vuetify 사용

const store = useBoardStore()
store.initialize()

app.mount('#app')
