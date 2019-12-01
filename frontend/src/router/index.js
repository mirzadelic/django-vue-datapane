import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Entry from '@/components/Entry'
import CSVParser from '@/components/CSVParser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/entry',
      name: 'Entry',
      component: Entry
    },
    {
      path: '/csv-parser',
      name: 'CSVParser',
      component: CSVParser
    }
  ]
})
