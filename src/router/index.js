import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from "@/views/Login" //登陆

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/Register',
    name: 'Register',
    component: () => import('../views/Register')
  },
  {
    path: '/Homepage',
    name: 'Homepage',
    component: () => import('../views/Homepage')
  }
  , {
    path: '/Studentinfo',
    name: 'Studentinfo',
    component: () => import('../views/Studentinfo')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
