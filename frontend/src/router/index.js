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
import StudentApplications from '@/components/StudentApplications.vue'
import AdminStudentApplications from '@/components/AdminStudentApplications.vue'
import CompanyDriveApplications from '@/components/CompanyDriveApplications.vue'
import ShortlistedStudents from '@/components/ShortlistedStudents.vue'
import RegisteredStudent from '@/components/RegisteredStudent.vue'


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



    // ADMIN ROUTES H ___________________________
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
          path: 'registered_students',
          component: RegisteredStudent
        },
        {
          path: 'student_applications',
          component: AdminStudentApplications
        },
        {
          path: 'drive/:id',
          component:DrivesDetails
        }
      ]
    },

    // COMPANY HH_______________________
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
          path: 'shortlisted_students',
          component: ShortlistedStudents
        },
        {
          path: 'create_drives',
          component: CreateDrives
        },
        {
          path: 'drive/:id/applications',
          component: CompanyDriveApplications
        },
        {
          path: 'drive/:id',
          component:DrivesDetails
        }
      ]
    },

// STUDENT ROUTE H ______________________

    {
      path:'/student',
      name: 'student',
      redirect:'/student/drives'
    },
    {
      path: '/student',
      
      component: () => import('../views/Student/StuDashView.vue'),
      
      children: [
        {
          path:'profile',
          component:StudentProfile
        },
        {
          path:'applications',
          component:StudentApplications
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
