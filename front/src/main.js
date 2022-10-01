import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios"
import router from './router'
import mitt from 'mitt'

// Vue3 新發明的工廠函式 = =??
const Factory = createApp(App)
Factory.use(router)
// Factory.use(router).use(store)
Factory.config.globalProperties.$http = axios
Factory.config.globalProperties.$emitter = mitt()
Factory.mount('#app')
