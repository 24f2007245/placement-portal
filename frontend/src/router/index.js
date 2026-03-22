import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },

    // auth
    {
      path: '/register',
      name: 'register',
      
      component: () => import('../views/Auth/RegisterView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Auth/LoginView.vue')
    },

    // admin
    {
      path: '/admin/dash',
      name: 'admin_dash',
      component: () => import('../views/Admin/AdminDashView.vue')
    },

    // company
    {
      path: '/company/dash',
      name: 'company_dash',
      component: () => import('../views/Company/ComDashView.vue')
    },
    {
      path: '/student/dash',
      name: 'student_dash',
      component: () => import('../views/Student/StuDashView.vue')
    },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')
  const publicPaths = ['/', '/login', '/register']

  if (!token && !publicPaths.includes(to.path)) {
    return next('/login')
  }

  if (to.path.startsWith('/admin') && role !== 'admin') {
    return next('/login')
  }

  if (to.path.startsWith('/student') && role !== 'student') {
    return next('/login')
  }

  if (to.path.startsWith('/company') && role !== 'company') {
    return next('/login')
  }

  next()
})

export default router
