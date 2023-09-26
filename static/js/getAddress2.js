import useModelList from "./useModelList.js";
import { convertVietnamese, convertType } from "./utils.js";

const { createApp, ref, watch } = Vue;
const { createVuetify } = Vuetify;

const vuetify = createVuetify();
const app = createApp({
  setup() {
    const addresses = ref([]);
    const isLoadingAddresses = ref(false);

    // Get wards
    const {
      isLoading,
      results: wards,
      getResults: getWards,
    } = useModelList("wards");

    const searchToAddresses = async (keyword) => {
      // from search keyword, return addresses
      const { wardKeyword, districtKeyword } = getSearchKeywords(keyword);
      if (wardKeyword) await getWards({ search: wardKeyword, limit: 100 });
      if (districtKeyword)
        wards.value = districtFilter(districtKeyword, wards.value);
      addresses.value = wardsToAddresses(wards.value);
    };

    // time between searches (miliseconds)
    const Delta = 500;
    const isStopTyping = ref(false);
    let keyword = "";
    let typingTimer;

    const onSearch = (search) => {
      keyword = search;
      clearTimeout(typingTimer);
      // Start counting again, after delta miliseconds then raise flag stop typing
      typingTimer = setTimeout(() => {
        isStopTyping.value = true;
      }, Delta);
    };

    watch(isStopTyping, (newValue) => {
      if (newValue)
        keyword ? searchToAddresses(keyword) : (addresses.value = []);
      isStopTyping.value = false;
    });

    return {
      addresses,
      isLoading,
      onSearch,
    };
  },
  delimiters: ['[[', ']]'],
});
app.use(vuetify).mount("#getAddress2");

const getSearchKeywords = (search) => {
  // From search keyword, calculate to get keywords for ward and district
  const searchArray = search.split(",", 2);
  let wardKeyword, districtKeyword;
  wardKeyword = searchArray[0].trim();
  if (searchArray.length > 1) districtKeyword = searchArray[1].trim();

  return { wardKeyword, districtKeyword };
};

const wardsToAddresses = (wards) => {
  // From wards, get full addresses
  let addresses = [];
  wards.forEach((w) => {
    const wardName = convertType(w.type, 3) + " " + w.name;
    const districtName =
      convertType(w.district.type, 2) + " " + w.district.name;
    const provinceName =
      convertType(w.province.type, 1) + " " + w.province.name;
    const address = wardName + ", " + districtName + ", " + provinceName;
    addresses.push(address);
  });

  return addresses;
};

const districtFilter = (districtKeyword, wards) => {
  // use districtKeyword to filter wards
  return wards.filter((w) =>
    w.district.name_en
      .toLowerCase()
      .includes(convertVietnamese(districtKeyword))
  );
};
