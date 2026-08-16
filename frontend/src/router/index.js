import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
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
      component: () => import('@/views/Admin/AdminDashView.vue'),
      children: [
        {
          path: 'drives',
          component: () => import('@/components/Drives.vue')
        },
        {
          path: 'company_application',
          component: () => import('@/components/CompanyApplication.vue')
        },
        {
          path: 'registered_company',
          component: () => import('@/components/RegisteredCompany.vue')
        },
        {
          path: 'registered_students',
          component: () => import('@/components/RegisteredStudent.vue')
        },
        {
          path: 'student_applications',
          component: () => import('@/components/AdminStudentApplications.vue')
        },
        {
          path: 'hired_students',
          component: () => import('@/components/AdminHiredStudents.vue')
        },
        {
          path: 'drive/:id',
          component: () => import('@/components/DrivesDetails.vue')
        },
        {
          path: 'past_drives',
          component: () => import('@/components/PastDrives.vue')
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
      component: () => import('@/views/Company/ComDashView.vue'),
      children: [
        {
          path: '',
          redirect: 'view_drives'
        },
        {
          path: 'view_drives',
          component: () => import('@/components/ViewDrives.vue')
        },
        {
          path: 'shortlisted_students',
          component: () => import('@/components/ShortlistedStudents.vue')
        },
        {
          path: 'create_drives',
          component: () => import('@/components/CreateDrives.vue')
        },
        {
          path: 'drive/:id/applications',
          component: () => import('@/components/CompanyDriveApplications.vue')
        },
        {
          path: 'drive/:id',
          component: () => import('@/components/DrivesDetails.vue')
        },
        {
          path: 'profile',
          component: () => import('@/components/CompanyProfile.vue')
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
      
      component: () => import('@/views/Student/StuDashView.vue'),
      
      children: [
        {
          path:'profile',
          component: () => import('@/components/StudentProfile.vue')
        },
        {
          path:'applications',
          component: () => import('@/components/StudentApplications.vue')
        },
        {
          path:'drives',
          component: () => import('@/components/Drives.vue')
        },
        {
          path:'past_drives',
          component: () => import('@/components/PastDrives.vue')
        }
      ]
    },
    {
      path: '/drive/:id',
      name: 'drive_details',
      component: () => import('@/components/DrivesDetails.vue')
    },
    {
      path: '/company/:id',
      name: 'company_details',
      component: () => import('@/components/CompanyDetails.vue')
    }
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
