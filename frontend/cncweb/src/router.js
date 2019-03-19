import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Navbar from '@/views/Navbar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: Home,
        navbar: Navbar
      },
    },
  ]
})
