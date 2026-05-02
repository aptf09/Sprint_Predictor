# AI Transparency Document — Sprint Time Predictor

**Project:** Sprint Time Predictor  
**Author:** Aparajith Suresh  
**Version:** 1.0  
**Date:** 2026  

---

## 1. What This Model Does

This project uses a Random Forest Regression model to predict an athlete's 100m sprint time based on a set of physical and lifestyle inputs. The model takes in factors such as age, height, weight, sleep, hydration, training frequency, strength metrics, and reaction time, and outputs a predicted sprint time in seconds.

The goal is to help athletes and coaches understand which factors most influence sprint performance, and to provide a data-driven estimate of expected race times.

---

## 2. How It Was Built

### Model Type
Random Forest Regressor (via scikit-learn)

### Training Data
The model was trained on a synthetically generated dataset of 150 athlete profiles. The dataset was created to reflect realistic relationships between training factors and sprint performance, based on established sports science knowledge. It covers athletes aged 12–25.

### Key Design Decisions
- A Random Forest was chosen over a single Decision Tree to reduce overfitting and improve prediction accuracy
- The dataset was split 75/25 into training and validation sets using `train_test_split`
- `random_state=1` was used throughout to ensure reproducibility

### Model Performance
- **Mean Absolute Error (MAE): 0.12 seconds**
- This means the model's predictions are within 0.12 seconds of the actual time on average

---

## 3. Limitations

- **Synthetic data:** The training data was computationally generated, not collected from real athletes. This means the model may not capture all the nuances of real-world athletic performance.
- **Limited features:** Many factors that affect sprint performance — such as muscle fibre composition, technique, weather conditions, and mental state — are not included in this model.
- **Age range:** The model is trained on athletes aged 12–25 and may produce less accurate predictions outside this range.
- **Small dataset:** 150 rows is a relatively small dataset for machine learning. A larger, real-world dataset would significantly improve accuracy.
- **No professional validation:** This model has not been validated by sports scientists or professional coaches. It should not be used as a substitute for professional athletic assessment.

---

## 4. Potential Biases

- The synthetic dataset was generated with assumptions about how each factor influences sprint time. These assumptions, while grounded in general sports science, may not reflect the experience of all athletes equally.
- The dataset does not account for gender differences in athletic performance, which can be significant in sprint events.
- Athletes from different training backgrounds, climates, or cultures may not be well represented in the data.

---

## 5. Ethical Considerations

- **Not a professional tool:** This model is built for educational purposes and personal exploration. It should not be used to make high-stakes decisions about an athlete's training, selection, or career.
- **Data privacy:** If this model is adapted to use real athlete data in the future, appropriate consent and data protection measures must be in place.
- **Fairness:** Users should be aware that the model's predictions are based on population-level patterns and may not accurately reflect individual circumstances.
- **Transparency:** The dataset, model code, and this document are all publicly available on GitHub to ensure full transparency about how the model works.

---

## 6. Intended Use

✅ Personal exploration of how lifestyle and training factors relate to sprint performance  
✅ Educational demonstration of machine learning applied to sports science  
✅ Portfolio project showcasing Python and ML skills  

❌ Professional athletic assessment  
❌ Selection or exclusion of athletes from teams or competitions  
❌ Medical or physiological advice  

---

## 7. How to Use Responsibly

- Treat predictions as estimates, not facts
- Use the model as a starting point for reflection on training habits, not as a definitive measure of performance
- Always consult a qualified coach or sports scientist for professional guidance
- If adapting this project with real data, ensure proper ethical approval and data consent

---

## 8. Future Improvements

- Collect real athlete data with appropriate consent to replace the synthetic dataset
- Add more features such as training intensity, weather conditions, and technique scores
- Include gender as a variable with appropriate handling
- Expand the age range and dataset size
- Build a simple user interface for easier input and prediction

---

*This document was produced in line with AI transparency best practices as taught by Anthropic Academy's AI Fluency programme.*
