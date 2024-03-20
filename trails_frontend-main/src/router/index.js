import { createRouter, createWebHashHistory } from 'vue-router'
import TrailList from '../views/TrailList.vue'
import NationalParkList from '../views/NationalParkList.vue'
import GetSelfie from '../views/GetSelfie.vue'
import TrailDetail from '../views/TrailDetail.vue'

const routes = [
  {
    path: '/',
    component: TrailList
  },
  {
    path: '/list',
    redirect: '/'
  },
  {
    path: '/nationalParkList',
    component: NationalParkList
  },
  {
    path: '/details',
    component: TrailDetail
  },
  {
    path: '/PhotoShop',
    component: GetSelfie
  }
]

export default createRouter({
  history: createWebHashHistory(),
  routes
})
