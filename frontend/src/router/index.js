import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "/ome",
    component: Home,
    meta: {
      title: 'LPL'
    }
  }
];

const router = new VueRouter({
  routes
});

export default router;
