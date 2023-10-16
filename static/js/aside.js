const { createApp, ref } = Vue;

const app = createApp({
    setup() {
        let isJustClickLink = false;

        const links = ref([
            {
                title: "Giới Thiệu",
                target: "intro",
                active: true,
                scrollYBuffer: 300,
            },
            {
                title: "Dữ Liệu",
                target: "APIdata",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "Ứng Dụng 1",
                target: "application-1",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "Ứng Dụng 2",
                target: "application-2",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "Tham Khảo",
                target: "references",
                active: false,
                scrollYBuffer: 600,
            },
        ]);

        const linksEn = ref([
            {
                title: "Introduction",
                target: "intro",
                active: true,
                scrollYBuffer: 300,
            },
            {
                title: "Data",
                target: "APIdata",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "Use Case 1",
                target: "application-1",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "Use Case 2",
                target: "application-2",
                active: false,
                scrollYBuffer: 0,
            },
            {
                title: "References",
                target: "references",
                active: false,
                scrollYBuffer: 600,
            },
        ]);

        const onActive = (link) => {
            isJustClickLink = true;

            document.getElementById(link.target).scrollIntoView({
                behavior: "smooth",
            });
            links.value.forEach((l) => (l.active = l == link ? true : false));

            setTimeout(() => (isJustClickLink = false), 500);
        };

        window.onscroll = () => {
            let current;

            links.value.forEach((l) => {
                const targetElement = document.getElementById(l.target);
                const elementTop = targetElement.offsetTop;
                if (scrollY >= elementTop - 60 - l.scrollYBuffer) {
                    current = l;
                }
            });

            if (!isJustClickLink)
                links.value.forEach(
                    (l) => (l.active = l == current ? true : false)
                );
        };

        return { links, linksEn, onActive };
    },
    delimiters: ['[[', ']]'],
});
app.mount("#aside");
