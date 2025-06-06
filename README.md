# 🧪 Food Pathogen Risk Simulator

A scientific web application for simulating the growth and risk level of foodborne pathogens based on environmental and handling variables. Built with Streamlit, this tool helps food safety professionals and researchers assess potential risks in food handling scenarios.

## 🌟 Features

- **Interactive Simulation**: Real-time pathogen growth modeling using the Gompertz growth model
- **Risk Assessment**: Color-coded risk level indicators (Low, Medium, High) with specific recommendations
- **Customizable Parameters**:
  - Food type selection (Poultry, Dairy, Produce, Seafood)
  - Temperature control monitoring (0-50°C)
  - Time abuse tracking (0-72 hours)
  - pH level analysis (3.5-7.5)
  - Water activity measurement (0.85-1.0)
- **Visual Analytics**: Dynamic growth curve visualization with Plotly
- **Data Export**: Download simulation results as CSV for further analysis
- **Real-time Updates**: Instant feedback on parameter changes
- **Responsive Design**: Works on both desktop and mobile devices

## 🚀 Quick Start

### Option 1: Local Development

1. Clone the repository:
```bash
git clone https://github.com/CireWire/FoodPathogenRiskSimulator.git
cd FoodPathogenRiskSimulator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

5. Open your browser and navigate to `http://localhost:8501`

### Option 2: Docker Deployment

1. Clone the repository:
```bash
git clone https://github.com/CireWire/FoodPathogenRiskSimulator.git
cd FoodPathogenRiskSimulator
```

2. Build and run using Docker Compose:
```bash
docker-compose up --build
```

3. Open your browser and navigate to `http://localhost:8501`

To stop the application:
```bash
docker-compose down
```

### Option 3: Visit App Site
Visit the live application at [Food Pathogen Risk Simulator](https://food-pathogen-risk-simulator.streamlit.app)

## 📊 Scientific Background

The simulator uses a modified Gompertz growth model to predict pathogen population growth based on environmental conditions. The risk assessment takes into account:

- Temperature abuse patterns and their impact on growth rates
- pH levels and their effect on microbial growth
- Water activity (aw) measurements and their influence on pathogen survival
- Time duration of exposure to risk factors
- Initial contamination levels and their progression
- Food matrix characteristics and their impact on growth

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Data Processing**: NumPy, SciPy
- **Visualization**: Plotly
- **Data Management**: Pandas

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Special thanks to the Streamlit team for their amazing framework
- Inspired by food safety research and best practices
- Developed by The Helix Corporation

## 📞 Support

If you find this project helpful, consider supporting its development:
[Buy Me A Coffee](https://ko-fi.com/cirewire) 