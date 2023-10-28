import { createRouter, createWebHistory } from 'vue-router'

import Home from "../views/Home.vue"
import SignUp from "../views/SignUp.vue"
import Login from "../views/Login.vue"
import ProductDetails from "../views/ProductDetails.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'Home-page',
        component: Home
    },
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
    {
        path: '/product/details/:id',
        name: 'Product-details-page',
        component: ProductDetails
    }
  ]
})

export default router
