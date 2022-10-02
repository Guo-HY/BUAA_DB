import Vue from 'vue'     //在页面中引入vue.js
import App from './App.vue'   //引入自定义组件
import router from './router'   //引入路由
import store from './store'
import axios from 'axios'
// 按需引入
// import { Button, Select, Link } from 'element-ui';
// 全部引入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// 全局设置尺寸,这里是默认small,弹框初始z-index为3000
// Vue.prototype.$ELEMENT = { size: 'small', zIndex: 3000 };
// Vue.use(Button)
// Vue.use(Select)
// Vue.use(Link)

// 全局引入
Vue.use(ElementUI);
// Vue.use(Element, { size: 'small', zIndex: 3000 });
Vue.prototype.$http = axios // 修改内部的$http为axios  $http.get(url) .post    ----使用
Vue.config.productionTip = false
/* 指定 axios 发送请求的目标后端地址的根路径，一般为后端服务器IP+端口，若有部署域名则可以是域名地址 */
// axios.defaults.baseURL = '/api';


new Vue({     // Vue全局实例
  router,     
  store,
  render: h => h(App)
}).$mount('#app')
