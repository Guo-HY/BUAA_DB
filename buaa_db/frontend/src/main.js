import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

/* 引入 axios 并挂载到 Vue 实例上 */
Vue.prototype.$axios = axios


/* 指定 axios 发送请求的目标后端地址的根路径，一般为后端服务器IP+端口，若有部署域名则可以是域名地址 */
axios.defaults.baseURL = '/api';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
