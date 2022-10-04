import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Home from '../components/Home'
import User from '../components/User'
import Student from "../components/Student"
import UserAdd from "../components/UserAdd"
import UserEdit from "../components/UserEdit"
import ChooseClass from "../components/ChooseClass"
import ChooseYes from "../components/ChooseYes"
import ChooseNo from "../components/ChooseNo"
import Login from "../views/Login"
import Register from "../views/Register"
import Homepage from "../views/Homepage"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/home'
  },
  {
    path: '/home',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/user',
    component: User,
    children:[
      {path:'add', component:UserAdd}, //用户的添加 路由
      {path:'edit', component:UserEdit}
    ]
  },
  {
    path: '/student',
    component: Student
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/chooseclass',
    component: ChooseClass,
    children:[
      {path:'choose', component:ChooseYes},
      {path:'withdraw', component:ChooseNo}
    ]
  }
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
