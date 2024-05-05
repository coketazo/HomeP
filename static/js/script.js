const sections = document.querySelectorAll('.content');

window.addEventListener('scroll', () => {
	let currentSectionId = '';
	sections.forEach(section => {
		const sectionTop = section.offsetTop;
		const sectionHeight = section.clientHeight;
		const screenHeight = window.innerHeight;
		const scrollPosition = window.scrollY;
		if (scrollPosition >= sectionTop - screenHeight / 2 && scrollPosition < sectionTop + sectionHeight - screenHeight / 2) {
			currentSectionId = section.getAttribute('id');
		}
	});

	const navLinks = document.querySelectorAll('nav a');
	navLinks.forEach(link => {
		link.classList.remove('active');
		if (link.getAttribute('href').substring(1) === currentSectionId) {
			link.classList.add('active');
		}
	});
});

document.querySelectorAll('nav a').forEach(anchor => {
	anchor.addEventListener('click', function (e) {
		e.preventDefault();

		const targetId = this.getAttribute('href').substring(1);
		const targetElement = document.getElementById(targetId);

		targetElement.scrollIntoView({
			behavior: 'smooth',
			block: 'center'
		});
	});
});