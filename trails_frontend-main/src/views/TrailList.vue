<template>
  <div>
    <search-bar ref="searchBarRef"></search-bar>
    <div class="list-container">
      <v-breadcrumbs :items="breadcrumbs">
        <template v-slot:title="{ item }">
          {{ item.title.toUpperCase() }}
        </template>
      </v-breadcrumbs>
      <div class="header">Top Trails</div>
      <ul v-if="trailList.length > 0">
        <li
          v-for="(item, index) in trailList"
          :key="item.key"
          class="trail-item-container"
          @click="goToDetail(item.id)"
        >
          <trail-card :index="index" :info="item"></trail-card>
        </li>
        <div class="pagination-info" v-if="!noMoreTrails">
          <v-btn class="showMore-btn" @click="showMoreTrails">
            Show more trails
          </v-btn>
          <span class="page-info">
            Showing results 1-{{ curPage * pageSize }} of {{ totalNumber }}
          </span>
        </div>
        <div class="pagination-info" v-else>
          Loaded {{ totalNumber }} trails
        </div>
      </ul>
      <div v-else-if="!isListLoading" class="noTrail-view">
        <span class="headsup">No Results found</span>
        <span class="reminds">
          Adjust your filters or clear them to see trails
        </span>
        <v-btn class="clear-btn" @click="clearFilter">Clear filters</v-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import TrailCard from './components/TrailCard.vue'
import SearchBar from './components/SearchBar.vue'
import requests from '../services/requests'
import { trails } from '../services/apis'
const router = useRouter()

const searchBarRef = ref(null)
const trailList = ref([])
const curPage = ref(1)
const pageSize = ref(10)
const totalNumber = ref(0)
const totalPages = ref(0)
const isListLoading = ref(false)
const noMoreTrails = ref(false)
const params = ref({
  state: 'California',
  curPage: curPage.value,
  pageSize: pageSize.value
})

const getTrailList = (params) => {
  isListLoading.value = true
  requests
    .post(trails.list, params)
    .then((res) => {
      if (res.status != '200') {
        return
      }
      const { data, pageVO } = res.data
      totalNumber.value = pageVO.totalCount
      totalPages.value = pageVO.totalPages
      trailList.value = trailList.value.concat(
        data.map((trail) => {
          const randomNum = Math.floor(Math.random() * 200)
          return {
            id: trail._id,
            trailName: trail.name !== 'NA' ? trail.name : '--',
            parkName: trail.location !== 'NA' ? trail.location : '--',
            length: trail.totalDistance !== 'NA' ? trail.totalDistance : '--',
            desctiption: '',
            rank: trail.rank !== 'NA' ? trail.rank : '--',
            green:
              trail.trailDifficultyList.accessRoad +
                trail.trailDifficultyList.accessRoad.white +
                trail.trailDifficultyList.accessRoad.green || '--',
            blue: trail.trailDifficultyList.blue || '--',
            diamond: trail.trailDifficultyList.black || '--',
            doubleDiamond:
              trail.trailDifficultyList.doubleBlackDiamond +
                trail.trailDifficultyList.proline || '--',
            trailsNum: trail.trailsNum,
            isBookmarked: false,
            imgName: `https://picsum.photos/id/${randomNum}/200/300`
          }
        })
      )
    })
    .finally((isListLoading.value = false))
}
getTrailList(params.value)

const breadcrumbs = [
  {
    title: 'Hiking',
    disabled: false,
    href: '#/list'
  },
  {
    title: 'United States',
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

const showMoreTrails = () => {
  if (curPage.value + 1 > totalPages.value) {
    noMoreTrails.value = true
    return
  }
  curPage.value += 1
}

const clearFilter = () => {
  searchBarRef.value.reset()
  getTrailList(params.value)
}

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
