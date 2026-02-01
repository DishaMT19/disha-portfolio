# Disha M T - Portfolio Website

A modern, responsive, and interactive personal portfolio website showcasing web development projects, skills, education, and contact information.

## 🌟 Features

- **Responsive Design** - Mobile-friendly layout that works on all devices
- **Dark/Light Theme Toggle** - Switch between dark and light modes
- **Smooth Animations** - Engaging scroll animations and transitions
- **Interactive Elements** - Particle background, custom cursor, ripple effects
- **Project Showcase** - Display of 3 featured projects with live demos and GitHub links
- **Skills Section** - Visual skill progression bars for frontend, backend, database, and tools
- **Timeline Education** - Educational background displayed in an interactive timeline
- **Contact Form** - Functional contact form with Flask backend integration
- **Certificate Modal** - Modal popup to view certificates
- **Loading Screen** - Professional loading animation
- **Back-to-Top Button** - Quick navigation to top of page
- **Social Media Links** - Integration with LinkedIn, GitHub, Instagram, and Twitter

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Advanced styling with CSS variables and animations
- **JavaScript (ES6+)** - Interactive functionality and animations
- **Particles.js** - Animated particle background
- **Font Awesome 6.4.0** - Icon library

### Backend
- **Python** - Backend logic
- **Flask** - Web framework for API endpoints
- **CSV** - Message storage

## 📁 Project Structure

```
Portfolio/
├── index.html                 # Main portfolio page
├── README.md                  # This file
├── contact/
│   ├── app.py                # Flask backend for contact form
│   ├── contact_messages.csv   # Contact messages storage
│   └── messages.csv           # Additional message records
├── aa.jpg                     # Profile picture
├── banner.png                 # KidsMart project banner
├── OIG1.jpeg                  # Josh Natural Candy project image
├── 06de4a7f-c306-48d4-9c26-8d262c0e3abe.webp  # Calculator project image
├── DISHA_MT_RESUME.pdf        # Resume file
├── Drishti certificate.pdf    # Certificate
├── certificate_20251562679920.pdf # ISRO Certificate
├── certificate hackathon.pdf  # Hackathon certificate
└── Research Methodologies and IPR.pdf # Course certificate
```

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.7+ (for running the Flask backend)
- Flask (`pip install flask`)

### Installation

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd Portfolio
   ```

2. **Set Up the Flask Backend** (Optional)
   ```bash
   cd contact
   pip install flask
   python app.py
   ```
   The backend will run on `http://127.0.0.1:5000`

3. **Open the Portfolio**
   - Open `index.html` in a web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     ```
   - Visit `http://localhost:8000`

## 📋 Sections

### Hero Section
- Welcoming introduction with profile picture
- Call-to-action buttons
- Social media links

### About Section
- Personal introduction
- Quick bio
- Key information (name, email, location, education)

### Skills Section
- **Frontend**: HTML5, CSS3, JavaScript, Angular.js
- **Backend**: Python, Java, Node.js, Flask
- **Database**: MySQL, MongoDB, PostgreSQL
- **Tools & Others**: Git, RESTful APIs, Responsive Design

### Projects Section
- **KidsMart E-commerce** - Children's products platform
- **Josh Natural Candy** - Natural confectioneries e-commerce
- **Scientific Calculator** - Advanced calculation tool with unit conversion

### Education Section
- Master of Computer Applications (MCA) - VTU
- Bachelor of Science - Mangalore University
- Pre-University - Karnataka
- SSLC

### Contact Section
- Contact information (location, email, phone)
- Functional contact form
- Message submission via Flask API

## ⚙️ Configuration

### Customization

1. **Update Personal Information** - Edit the following in `index.html`:
   - Name and title in the hero section
   - About section content
   - Contact information
   - Social media links

2. **Modify Skills** - Update skill names and percentages in the skills section

3. **Add/Remove Projects** - Add new project cards in the projects section

4. **Change Color Theme** - Modify CSS variables in the `<style>` section:
   ```css
   :root {
       --primary-light: #3b82f6;
       --accent-light: #06b6d4;
       /* ... other colors ... */
   }
   ```

5. **Update Certificates** - Modify the certificate modal content with your own certificates

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 991px
- **Mobile**: Below 768px

## 🔌 Backend Integration

The contact form submits to:
```
POST http://127.0.0.1:5000/api/contact/submit
```

**Payload:**
```json
{
  "name": "string",
  "email": "string",
  "message": "string"
}
```

**Response:**
- Success (200): Message saved
- Error: Error message returned

## 🎨 Features Breakdown

### Theme Toggle
- Click the moon/sun icon in the navigation bar to switch themes
- Preference is not persisted (resets on page refresh)

### Animations
- **Fade-in animations** on scroll
- **Particle background** that responds to mouse movement
- **Custom cursor** with hover effects
- **Ripple effect** on button clicks
- **Skill progress bars** with animated fills
- **Project card hover** effects

### Accessibility
- Semantic HTML structure
- ARIA labels where applicable
- Keyboard-navigable links
- Focus indicators on interactive elements

## 📞 Contact

- **Email**: mtdisha3@gmail.com
- **Phone**: +91 8073437014
- **Location**: Mangalore, Dakshina Kannada, Karnataka, India
- **LinkedIn**: [linkedin.com/in/disha-mt-19480b340](https://linkedin.com/in/disha-mt-19480b340)
- **GitHub**: [github.com/DishaMT19](https://github.com/DishaMT19)
- **Instagram**: [@mt_disha745](https://www.instagram.com/mt_disha745)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Particles.js** - For the beautiful particle animation library
- **Font Awesome** - For the comprehensive icon collection
- **Modern Web Technologies** - For enabling responsive and interactive web design

---

**Last Updated**: February 2026

**Portfolio Website**: Visit the live portfolio at your deployment URL
