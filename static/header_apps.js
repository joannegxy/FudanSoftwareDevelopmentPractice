

const app1 = Vue.createApp({});

// Register the component
app1.component('app1', app1);

// Mount the Vue instance
app1.mount('#app1');

const app2 = Vue.createApp({});

// Register the component
app2.component('app2', app2);

// Mount the Vue instance
app2.mount('#app2');