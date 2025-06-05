# 🧪 Food Pathogen Risk Simulator

A scientific web application for simulating the growth and risk level of foodborne pathogens based on environmental and handling variables. Built with Streamlit, this tool helps food safety professionals and researchers assess potential risks in food handling scenarios.

## 🌟 Features

- **Interactive Simulation**: Real-time pathogen growth modeling
- **Risk Assessment**: Color-coded risk level indicators
- **Customizable Parameters**:
  - Food type selection (Poultry, Dairy, Produce, Seafood)
  - Temperature control monitoring
  - Time abuse tracking
  - pH level analysis
  - Water activity measurement
- **Visual Analytics**: Dynamic growth curve visualization
- **Data Export**: Download simulation results for further analysis

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/CireWire/FoodPathogenRiskSimulator.git
cd food-pathogen-simulator
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

## 📊 Scientific Background

The simulator uses a modified Gompertz growth model to predict pathogen population growth based on environmental conditions. The risk assessment takes into account:

- Temperature abuse patterns
- pH levels and their impact on growth
- Water activity (aw) measurements
- Time duration of exposure
- Initial contamination levels

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

## 📞 Support

If you find this project helpful, consider supporting its development:
[Buy Me A Coffee](https://ko-fi.com/cirewire) 