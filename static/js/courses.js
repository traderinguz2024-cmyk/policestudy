document.addEventListener('DOMContentLoaded', function () {
    const buttons = Array.from(document.querySelectorAll('.filter-btn'));
    const searchInput = document.getElementById('searchInput');
    const cards = Array.from(document.querySelectorAll('.course-card'));
    const noResults = document.getElementById('noResults');

    if (!buttons.length || !searchInput || !cards.length || !noResults) {
        return;
    }

    let activeFilter = 'all';

    function applyFilters() {
        const query = searchInput.value.trim().toLowerCase();
        let visibleCount = 0;

        cards.forEach((card) => {
            const matchesFilter = activeFilter === 'all' || card.dataset.category === activeFilter;
            const haystack = card.dataset.title || '';
            const matchesSearch = !query || haystack.includes(query);
            const visible = matchesFilter && matchesSearch;

            card.style.display = visible ? 'flex' : 'none';
            if (visible) {
                visibleCount += 1;
            }
        });

        noResults.style.display = visibleCount ? 'none' : 'block';
    }

    buttons.forEach((button) => {
        button.addEventListener('click', function () {
            buttons.forEach((btn) => btn.classList.remove('active'));
            this.classList.add('active');
            activeFilter = this.dataset.filter;
            applyFilters();
        });
    });

    searchInput.addEventListener('input', applyFilters);
    applyFilters();
});
