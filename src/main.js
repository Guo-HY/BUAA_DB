import Vue from 'vue'     //在页面中引入vue.js
import App from './App.vue'   //引入自定义组件
import router from './router'   //引入路由
import store from './store'
import axios from 'axios'

Vue.prototype.$http = axios // 修改内部的$http为axios  $http.get(url) .post    ----使用
Vue.config.productionTip = false

new Vue({     // Vue全局实例
  router,     
  store,
  render: h => h(App)
}).$mount('#app')
