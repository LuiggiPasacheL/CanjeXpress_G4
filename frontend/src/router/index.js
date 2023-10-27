import { createRouter, createWebHistory } from 'vue-router'

import SignUp from "../views/SignUp.vue"
import Login from "../views/Login.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/sign-up',
      name: 'SignUp-page',
      component: SignUp,
    },
    {
      path: '/login',
      name: 'Login-page',
      component: Login,
    },
  ]
})

export default router
