import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Home from '../components/Home/Home'
import Login from "../views/Login"
import Community from "../components/Community"
import Group from "../components/Group"
import Post from "../components/Post"
import Profile from "../components/Profile"
import UserInfoView from "@/views/UserInfoView";
import DriftBottleView from "@/views/DriftBottleView";
import ActivityView from "@/views/ActivityView";
import DriftBottleContentView from "@/views/DriftBottleContentView";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    component: Login
  },
  {
    path:'/community',
    component:Community
  },
  {
    path:'/group',
    component:Group
  },
  {
    path:'/post',
    component:Post
  },
  {
    path: '/UserInfo',
    name: 'UserInfoView',
    component: UserInfoView
  },
  {
    path: '/Activity',
    name: 'ActivityView',
    component: ActivityView
  },
  {
    path: '/DriftBottles',
    name: 'DriftBottlesView',
    component: DriftBottleView
  },
  {
    path: '/DriftBottleContent',
    name: 'DriftBottleContentView',
    component: DriftBottleContentView
  },
  // {
  //   path: '/useradd',
  //   component: UserAdd
  // }
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  routes
})

export default router
