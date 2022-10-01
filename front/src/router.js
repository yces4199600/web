import { createRouter, createWebHashHistory } from 'vue-router'
import Admin from '@/page/Admin.vue'
import Index from '@/page/Index.vue'
import Cart from '@/page/Cart.vue'
import Login from '@/page/Login.vue'
import Signup from '@/page/Signup.vue'
const routes = [
  {
    path: '/index',
    redirect: {
      name: 'Index'
    }
  },
  {
    path: '/',
    name: 'Index',
    component: Index
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart

  }
]

const router = createRouter({
  history: createWebHashHistory(),
  linkExactActiveClass: 'active',
  routes
})

export default router;
