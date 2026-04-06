import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Drives from '@/components/Drives.vue'
import RegisteredCompany from '@/components/RegisteredCompany.vue'
import CompanyApplication from '@/components/CompanyApplication.vue'
import AdminDashView from '@/views/Admin/AdminDashView.vue'
import ComDashView from '../views/Company/ComDashView.vue'
import CreateDrives from '@/components/CreateDrives.vue'
import ViewDrives from '@/components/ViewDrives.vue'
import DrivesDetails from '@/components/DrivesDetails.vue'
import StudentProfile from '@/components/StudentProfile.vue'


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
      path: '/admin',
      name: 'admin',
      redirect: '/admin/drives'
    },
    {
      path: '/admin',
      component: AdminDashView,
      children: [
        {
          path: 'drives',
          component: Drives
        },
        {
          path: 'company_application',
          component: CompanyApplication
        },
        {
          path: 'registered_company',
          component: RegisteredCompany
        },
        {
          path: 'drive/:id',
          component:DrivesDetails
        }
      ]
    },

    // company
    {
      path: '/company',
      name: 'company',
      redirect: '/company/view_drives'
    },
    {
      path: '/company',
      component: ComDashView,
      children: [
        {
          path: '',
          redirect: 'view_drives'
        },
        {
          path: 'view_drives',
          component: ViewDrives
        },
        {
          path: 'create_drives',
          component: CreateDrives
        },
        {
          path: 'drive/:id',
          component:DrivesDetails
        }
      ]
    },
    {
      path: '/student',
      name: 'student',
      component: () => import('../views/Student/StuDashView.vue'),
      
      children: [
        {
          path:'profile',
          component:StudentProfile
        },
        {
          path:'drives',
          component:Drives
        }
      ]
    },
    {
      path: '/drive/:id',
      name: 'drive_details',
      component: DrivesDetails
    },
  ],
})

// router.beforeEach((to, next) => {
//   const token = localStorage.getItem('token')
//   const role = localStorage.getItem('role')
//   const publicPaths = ['/', '/login', '/register']

//   if (!token && !publicPaths.includes(to.path)) {
//     return next('/login')
//   }

//   if (to.path.startsWith('/admin') && role !== 'admin') {
//     return next('/login')
//   }

//   if (to.path.startsWith('/student') && role !== 'student') {
//     return next('/login')
//   }

//   if (to.path.startsWith('/company') && role !== 'company') {
//     return next('/login')
//   }

//   next()
// })

export default router
