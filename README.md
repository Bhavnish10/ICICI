# ICICI Bank Investment Analysis

## Overview
Comprehensive investment analysis and dashboard for ICICI Bank Limited, featuring financial metrics, valuation analysis, and interactive visualizations.

## Files Included

### 📊 Dashboard
- **[ICICI Bank Dashboard](https://bhavnish10.github.io/ICICI/)** - Interactive financial dashboard with real-time metrics
- **Local Access**: Open `ICICI_Bank_Dashboard.html` in your browser or run `python -m http.server 8081`

### 📄 Investment Thesis
- **[ICICI_Bank_Investment_Thesis.md](ICICI_Bank_Investment_Thesis.md)** - Comprehensive investment analysis document
- **Recommendation**: BUY with >15% annualized returns target
- **Investment Horizon**: 3-5 years

### 📑 Source Data
- **[ICICI_Bank_Investment_Report.pdf](ICICI_Bank_Investment_Report.pdf)** - Original investment report
- **[icici_report_extracted.txt](icici_report_extracted.txt)** - Extracted text from PDF

### 🔧 Tools
- **[extract_pdf.py](extract_pdf.py)** - PDF text extraction script
- **Dependencies**: PyPDF2 library

## Key Financial Metrics

| Metric | Value | Trend |
|--------|-------|-------|
| PAT FY2025 | ₹47,227 Cr | +15% YoY |
| Return on Equity | 18.4% | Industry Leading |
| Gross NPA | 1.67% | Improving |
| CET1 Ratio | 17.7% | Strong Capital Base |
| Net Interest Margin | 4.4-4.5% | Among Highest |

## Dashboard Features

### 📈 Interactive Charts
- Revenue & Profit Growth (5-year trend)
- Asset Quality Trends (NPA improvement)
- 5-Year DCF Projections (Base vs Bull case)
- Capital Efficiency Metrics (Portfolio distribution)

### 🎯 Key Sections
- **Overview**: Core KPIs and performance metrics
- **Financial Metrics**: Detailed financial analysis
- **Valuation**: DCF analysis and market comparison
- **Growth Drivers**: Expansion and digital initiatives
- **Risk Analysis**: Comprehensive risk assessment

### ✨ Interactive Elements
- Live data indicators
- Click animations on metrics
- Hover effects on charts
- Tab-based navigation
- Responsive design

## Investment Thesis Summary

ICICI Bank is positioned as a high-quality growth stock due to:
- **Strong Fundamentals**: 18.4% ROE, improving asset quality
- **Digital Leadership**: 93% digital transactions, 30M+ users
- **Growth Catalysts**: Retail expansion, SME lending, fee income diversification
- **Reasonable Valuation**: Trading at 17× earnings with 18%+ ROE

## Technical Setup

### Running Locally
```bash
# Clone the repository
git clone https://github.com/Bhavnish10/ICICI.git
cd ICICI

# Start local server
python -m http.server 8081

# Access dashboard at http://localhost:8081/ICICI_Bank_Dashboard.html
```

### PDF Extraction
```bash
# Extract text from PDF
python extract_pdf.py
```

## Valuation Analysis

### DCF Results
- **Intrinsic Value**: ₹1,030 per share
- **Market Price**: ₹1,278 per share
- **Premium**: 24% to intrinsic value
- **Expected Returns**: >15% CAGR over 3-5 years

### Scenarios
- **Base Case**: 12% PAT CAGR → 15% annualized returns
- **Bull Case**: 15% PAT CAGR → 20%+ annualized returns

## Risk Factors

1. **Economic Slowdown**: Impact on loan volumes and NPAs
2. **Regulatory Changes**: Capital requirements, fee caps
3. **Interest Rate Volatility**: NIM compression risk
4. **Competitive Pressure**: Fintech disruption
5. **Asset Quality Shocks**: Corporate default risk

## Repository Structure

```
ICICI/
├── docs/
│   └── index.html              # GitHub Pages dashboard
├── ICICI_Bank_Dashboard.html   # Main dashboard file
├── ICICI_Bank_Investment_Thesis.md
├── ICICI_Bank_Investment_Report.pdf
├── extract_pdf.py
├── icici_report_extracted.txt
└── README.md
```

## Live Demo

**Dashboard**: https://bhavnish10.github.io/ICICI/

## Disclaimer

This investment analysis is based on publicly available financial data and should not be considered as financial advice. Investors should conduct their own due diligence and consider their risk tolerance before making investment decisions.

---

*Last Updated: March 2026*
