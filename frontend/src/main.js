import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import "./plugins/element.js";

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  window.document.title =
    to.meta.title == undefined ? "LPL" : to.meta.title;
  next();
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
