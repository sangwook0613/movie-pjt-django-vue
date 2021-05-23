import Vue from 'vue'
import VueRouter from 'vue-router'

// import Home from '@/views/Home.vue'

// Accounts
import Signup from '@/components/accounts/Signup'
import Login from '@/components/accounts/Login'
import Profile from '@/components/accounts/Profile'
import LikeMovieSelect from '@/components/accounts/LikeMovieSelect'
// Movies
import Movie from '@/views/Movie'
import MovieDetail from '@/components/movies/MovieDetail'
// Community
import Community from '@/views/Community'
import ReviewDetail from '@/components/community/ReviewDetail'
import ReviewForm from '@/components/community/ReviewForm'
// Search
import Search from '@/views/Search'
// import SearchDetail from '@/components/search/SearchDetail'


Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/movie/:movieId/review',
    name: 'ReviewForm',
    component: ReviewForm,
  },
  {
    path: '/movie/:movieId/review/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/profile/:username',
    name: 'Profile',
    component: Profile,

    children: [
      { path: 'movies/:movieId', // 앞에 / 를 선언하면 부모 url 뒤에 붙지 않는다.
        name: 'ProfileMovieDetail',
        component: MovieDetail,
      },
    ],
  },
  {
    path: '/movie',
    name: 'Movie',
    component: Movie,
    
    // 중첩된 라우트는 children 속성으로 하위 라우트를 정의할 수 있다.
    children: [
      { path: ':movieId',
        name: 'MovieDetail',
        component: MovieDetail,
        // components: {
        //   default: '',
        //   a: MovieDetail,
        // }
      },
    ],
  },
  {
    path: '/search/',
    name: 'Search',
    component: Search,
    props: (route) => ({ 
      query: route.query.q
    }),
  },
  {
    path: '/signup/likemovies/',
    name: 'LikeMovieSelect',
    component: LikeMovieSelect,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router

// 로그인 한 상태 -> Logout
// 로그아웃 한 상태 -> Login, Signup

// router.beforeEach((to, from, next) => {
//   // console.log(to)
//   // console.log(to.name)
//   // console.log(from)
//   // next()
  
//   //1-1. 로그인이 필요한 컴포넌트
//   const authPages = [
//     'TodoList', 
//     'CreateTodo',
//   ]
//   //1-2. 로그아웃이 필요한 컴포넌트(로그인 상태가 아닌 경우에 방문해야 하는 컴포넌트)
//   const publicPages = [
//     'Login', 
//     'Signup',
//   ]

//   //2. 
//   // 가려고 하는 곳(to)이 로그인이 필요한 곳인지 여부를 체크하자 -> true / false 
//   const authRequired = authPages.includes(to.name)
//   // 가려고 하는 곳이 로그인이 필요하지 않은 곳은지 여부를 체크하자 -> true / false 
//   const authNotRequired = publicPages.includes(to.name)
//   // 로그인이 되어있는지 여부를 체크하자 -> true / false
//   const isLoggedIn = localStorage.getItem('jwt') ? true : false


//   //3. 
//   //3-1. 만약 로그인이 필요한 컴포넌트인데 로그인이 안되어 있는 경우에 강제로 가려고 하면?
//   if (authRequired && !isLoggedIn) {
//     // 로그인을 할 수 있도록 (가드) -> Login 컴포넌트로 보내자
//     next({ name: 'Login' })
//   //3-2. 만약 로그인이 필요하지 않은 컴포넌트인데 로그인이 되어있는 상태에서 강제로 가려고 하면?
//   } else if (authNotRequired && isLoggedIn) {
//     next({ name: 'TodoList' })
//   } else {
//     next()
//   }
// })
