import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Home from '../components/Home/Home'
import Student from "../components/Student"
import ChooseClass from "../components/ChooseClass"
import ChooseYes from "../components/ChooseYes"
import ChooseNo from "../components/ChooseNo"
import Login from "../views/Login"
import Register from "../views/Register"
import Community from "../components/Community"
import Group from "../components/Group"
import Post from "../components/Post"
import Profile from "../components/Profile"

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
    path:'/profile',
    component:Profile
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
