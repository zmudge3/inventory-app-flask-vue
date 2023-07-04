import { createRouter, createWebHistory } from 'vue-router'
import Containers from '../components/Containers.vue'
import ContainerForm from '../components/ContainerForm.vue'
import ContainerItems from '../components/ContainerItems.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Containers',
      component: Containers,
    },
    {
      path: '/containers/:containerID',
      name: 'ContainerItems',
      component: ContainerItems,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router
