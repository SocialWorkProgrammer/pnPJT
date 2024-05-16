import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

// `createPersistedState` 사용하여 플러그인 등록
pinia.use(createPersistedState())

app.use(pinia)
app.use(router)

app.mount('#app')
