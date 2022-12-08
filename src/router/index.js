import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Home from '../components/Home/Home'
import Login from "../views/Login"
import Community from "../components/Community"
import Group from "../components/Group"
import Post from "../components/Post"
import UserInfoView from "@/views/UserInfoView";
import DriftBottleView from "@/views/DriftBottleView";
import ActivityView from "@/views/ActivityView"
import MySendDriftBottlesView from "@/views/MySendDriftBottlesView";
import MyRepliedBottlesView from "@/views/MyRepliedBottlesView";
import MyReceivedBottleReplysView from "@/views/MyReceivedBottleReplysView";

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
    path: '/MyRepliedBottles',
    component: MyRepliedBottlesView
  },
  {
    path: '/MyReceivedBottleReplys',
    component: MyReceivedBottleReplysView
  },
  {
    path: '/MySendDriftBottles',
    component: MySendDriftBottlesView
  },
  {
    path: '/DriftBottles',
    name: 'DriftBottleView',
    component: DriftBottleView
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
