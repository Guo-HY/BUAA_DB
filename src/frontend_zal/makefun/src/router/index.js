import { createRouter, createWebHistory } from 'vue-router'
import HomePageView from "@/views/HomePageView";
import UserInfoView from "@/views/UserInfoView";
import DriftBottleView from "@/views/DriftBottleView";
import ActivityView from "@/views/ActivityView";
import DriftBottleContentView from "@/views/DriftBottleContentView";

const routes = [
  {
    path: '/',
    name: 'HomePageView',
    component: HomePageView
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
