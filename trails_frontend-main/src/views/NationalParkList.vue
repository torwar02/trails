<template>
  <div>
    <div class="list-container">
      <v-breadcrumbs :items="breadcrumbs">
        <template v-slot:title="{ item }">
          {{ item.title.toUpperCase() }}
        </template>
      </v-breadcrumbs>
      <ul>
        <li
          v-for="(item, index) in trailList"
          :key="item.key"
          class="trail-item-container"
          @click="goToDetail(item.id)"
        >
          <trail-card :index="index" :info="item"></trail-card>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import TrailCard from './components/TrailCard.vue'
const router = useRouter()

const trailList = ref([
  {
    national_park: 'Big Bend National Park',
    state: 'Texas (TX)',
    trail: 'Terlingua',
    activity: 'Ghost Towns',
    rating: '4.0',
    comments: [
      {
        comment_title: 'COWBOY LIVIN',
        comment_ratings: '5.0 of 5 bubbles',
        comment_text:
          'Texas style wild wild west for sure. I stayed in a Bed & Breakfast that ran off a generator and had no indoor plumbing and I must say I had the time of my life. I go there often and leave feeling like Belle Starr every time'
      }
    ]
  }
])
const curPage = ref(1)
const pageSize = ref(10)
const params = ref({
  state: 'California',
  curPage: curPage.value,
  pageSize: pageSize.value
})

const breadcrumbs = [
  {
    title: 'National Park',
    disabled: false,
    href: '#/list'
  },
  {
    title: 'ALL',
    disabled: false,
    href: '#/details'
  }
]
watch(
  curPage,
  () => {
    params.value.curPage = curPage.value
    getTrailList(params.value)
  },
  { deep: true }
)

const goToDetail = (id) => {
  router.push('details', { id })
}
</script>

<style lang="less" scoped>
.list-container {
  width: 70%;
  margin: 0 auto;
  .header {
    font-size: 28px;
    font-weight: bolder;
    color: #444444;
    margin-bottom: 18px;
  }
  .trail-item-container {
    list-style: none;
    margin-bottom: 32px;
    cursor: pointer;
    padding: 16px;
    border-radius: 6px;
  }
  .trail-item-container:hover {
    transition: all 0.3s;
    background-color: #f1f1f1;
  }
  .noTrail-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
    margin-top: 48px;
    .headsup {
      font-size: 28px;
      color: #252525;
      font-weight: bolder;
    }
    .reminds {
      color: #888888;
    }
    .clear-btn {
      background-color: #00c853;
      color: #ffffff;
      font-weight: bolder;
    }
  }
  .pagination-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 24px;
    gap: 18px;
    .showMore-btn {
      background-color: #00c853;
      color: #ffffff;
      font-weight: bolder;
    }
    .page-info {
      color: #888888;
    }
  }
}
</style>
