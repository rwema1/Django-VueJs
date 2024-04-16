<template>
  <div>
    <h2 v-if="user">Hello, {{ user.name }}<br></h2>
    <h2 v-else>Hello, Log in to view the dashboard</h2>
  </div>
</template>

<script> 
import { mapGetters } from 'vuex';

export default {
  name: 'HomePage',
  computed: {
    ...mapGetters(['user'])
  }
}
</script>