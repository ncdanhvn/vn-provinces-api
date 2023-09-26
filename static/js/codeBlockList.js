const { createApp, ref, watch } = Vue;
const { createVuetify } = Vuetify;

const codeBlocks1 = [
    {
        path: "provinces/",
        query: "?basic=true&limit=100",
    },
    {
        path: "provinces/",
        query: "ID",
    },
    {
        path: "districts/",
        query: "?province_id=ID&basic=true&limit=100",
    },
    {
        path: "districts/",
        query: "ID",
    },
    {
        path: "wards/",
        query: "?district_id=ID&basic=true&limit=100",
    },
];

const vuetify = createVuetify();
const app = createApp({
    setup() {
        const getUrl = (index) => "/api/" + codeBlocks1[index].path;
        const getQuery = (index) => codeBlocks1[index].query;
        const getFullUrl = (index) =>
            "https://vnprovinces.pythonanywhere.com" +
            getUrl(index) +
            getQuery(index);

        const snackbar = ref(false);
        const copyText = (index) => {
            navigator.clipboard.writeText(getFullUrl(index));
            snackbar.value = true;
        };
        return {
            copyText,
            getFullUrl,
            getUrl,
            getQuery,
            snackbar,
        };
    },
    delimiters: ['[[', ']]'],
});
app.use(vuetify).mount("#code-block-list");

const codeBlocks2 = [
    {
        path: "wards/",
        query: "?search=tên_xã_cần_tìm&limit=100",
    },
];

const app2 = createApp({
    setup() {
        const getUrl = (index) => "/api/" + codeBlocks2[index].path;
        const getQuery = (index) => codeBlocks2[index].query;
        const getFullUrl = (index) =>
            "https://vnprovinces.pythonanywhere.com" +
            getUrl(index) +
            getQuery(index);

        const snackbar = ref(false);
        const copyText = (index) => {
            navigator.clipboard.writeText(getFullUrl(index));
            snackbar.value = true;
        };
        return {
            copyText,
            getFullUrl,
            getUrl,
            getQuery,
            snackbar,
        };
    },
    delimiters: ['[[', ']]'],
});
app2.use(vuetify).mount("#code-block-list-2");

const codeBlocks3 = [
    {
        path: "provinces/",
        query: "?type=C",
    },
    {
        path: "provinces/",
        query: "?ordering=-area&limit=5",
    },
    {
        path: "provinces/",
        query: "?number_plates=50",
    },
    {
        path: "provinces/",
        query: "?neighbours=1&ordering=-population&limit=1",
    },
    {
        path: "districts/",
        query: "?is_border=true&is_coastal=true",
    },
    {
        path: "districts/",
        query: "?wards_count=0",
    },
    {
        path: "regions/",
        query: "?ordering=-provinces_count",
    },
];

const app3 = createApp({
    setup() {
        const getUrl = (index) => "/api/" + codeBlocks3[index].path;
        const getQuery = (index) => codeBlocks3[index].query;
        const getFullUrl = (index) =>
            "https://vnprovinces.pythonanywhere.com" +
            getUrl(index) +
            getQuery(index);

        const snackbar = ref(false);
        const copyText = (index) => {
            navigator.clipboard.writeText(getFullUrl(index));
            snackbar.value = true;
        };
        return {
            copyText,
            getFullUrl,
            getUrl,
            getQuery,
            snackbar,
        };
    },
    delimiters: ['[[', ']]'],
});
app3.use(vuetify).mount("#code-block-list-3");
