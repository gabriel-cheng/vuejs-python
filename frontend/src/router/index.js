import { createRouter, createWebHistory } from 'vue-router'
function lazyLoad(view) {
  return import(`../views/${view}.vue`);
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: lazyLoad('Home')
    },
  ]
})

export default router
