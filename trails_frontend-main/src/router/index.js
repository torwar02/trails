import { createRouter, createWebHashHistory } from 'vue-router'
import TrailList from '../views/TrailList.vue'
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
    path: '/details',
    component: TrailDetail
  }
]

export default createRouter({
  history: createWebHashHistory(),
  routes
})
