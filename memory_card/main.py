from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
import light_theme as light_theme 




app = QApplication([])

# Устанавливаем начальную тему
app.setStyleSheet(light_theme.style)  # Начальная светлая тема

from main_window import *
from menu_window import * 

def toggle_theme():
    global current_theme
    if current_theme == "light":
        app.setStyleSheet(dark_theme.style)  # Устанавливаем тёмную тему
        current_theme = "dark"
    else:
        app.setStyleSheet(light_theme.style)  # Устанавливаем светлую тему
        current_theme = "light"

current_theme = (toggle_theme)  # Начальная тема

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне питання")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText("Відповісти")
    RadioGroup.setExclusive(False)
    for btn in radio_buttons:
        btn.setChecked(False)
    RadioGroup.setExclusive(True)

def check_result():
    RadioGroup.setExclusive(False)
    for btn in radio_buttons:
        if btn.isChecked():
            if btn.text() == lb_correct.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                btn.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_result()
        lb_result.show()
        show_result()
    else:
        new_question()
        show_question()

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1















#НАЧИНАЕТЬСЯ АНАРЪХИЯ





q1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
q5 = Question('Возраст', 'age', 'years', 'lifetime', 'years_old')
q6 = Question('Температура', 'temperature', 'Celsius', 'weather', 'degrees')
q7 = Question('Масса', 'weight', 'kilograms', 'body', 'kg')
q8 = Question('Рост', 'height', 'centimeters', 'body', 'cm')
q9 = Question('Скорость', 'speed', 'km/h', 'motion', 'velocity')
q10 = Question('Продолжительность', 'duration', 'minutes', 'time', 'length')
q11 = Question('Глубина', 'depth', 'meters', 'distance', 'depth_level')
q12 = Question('Ширина', 'width', 'centimeters', 'dimension', 'width_size')
q13 = Question('Дистанция', 'distance', 'meters', 'travel', 'distance_travelled')
q14 = Question('Темп', 'rate', 'events per minute', 'frequency', 'speed_of_occurrence')
q15 = Question('Площадь', 'area', 'square meters', 'size', 'area_space')
q16 = Question('Время', 'time', 'seconds', 'clock', 'elapsed_time')
q17 = Question('Энергия', 'energy', 'joules', 'power', 'work_done')
q18 = Question('Объем', 'volume', 'liters', 'container', 'capacity')
q19 = Question('Плотность', 'density', 'kg/m³', 'material', 'density_value')
q20 = Question('Сила', 'force', 'newtons', 'interaction', 'force_applied')
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
q21 = Question('Давление', 'pressure', 'pascals', 'force per area', 'pressure_value')
q22 = Question('Ток', 'current', 'amperes', 'electricity', 'electric_current')
q23 = Question('Напряжение', 'voltage', 'volts', 'electricity', 'electric_potential')
q24 = Question('Сопротивление', 'resistance', 'ohms', 'electricity', 'resistance_value')
q25 = Question('Магнитное поле', 'magnetic_field', 'teslas', 'magnetism', 'magnetic_strength')
q26 = Question('Температурный коэффициент', 'temperature_coefficient', 'per degree Celsius', 'material property', 'thermal_coefficient')
q27 = Question('Частота', 'frequency', 'hertz', 'wave motion', 'signal_frequency')
q28 = Question('Индуктивность', 'inductance', 'henries', 'electric circuits', 'inductor_value')
q29 = Question('Ёмкость', 'capacitance', 'farads', 'electric circuits', 'capacitor_value')
q30 = Question('Сила тока', 'current_strength', 'amperes', 'electricity', 'current_power')
q31 = Question('Мощность', 'power', 'watts', 'energy', 'energy_consumed')
q32 = Question('Скорость света', 'speed_of_light', 'meters per second', 'physics', 'light_velocity')
q33 = Question('Концентрация', 'concentration', 'mol/liter', 'chemistry', 'solution_strength')
q34 = Question('Обратная связь', 'feedback', 'unitless', 'control systems', 'feedback_ratio')
q35 = Question('Дельта времени', 'time_delta', 'seconds', 'time', 'time_difference')
q36 = Question('Коэффициент полезного действия', 'efficiency', 'percentage', 'energy systems', 'energy_efficiency')
q37 = Question('Работа', 'work', 'joules', 'physics', 'energy_transfer')
q38 = Question('Момент силы', 'torque', 'newton-meters', 'mechanics', 'rotational_force')
q39 = Question('Температура плавления', 'melting_point', 'Celsius', 'material science', 'melting_temperature')
q40 = Question('Температура кипения', 'boiling_point', 'Celsius', 'material science', 'boiling_temperature')
q41 = Question('Скорость звука', 'speed_of_sound', 'meters per second', 'acoustics', 'sound_velocity')
q42 = Question('Молекулярная масса', 'molecular_mass', 'grams per mole', 'chemistry', 'atomic_weight')
q43 = Question('Концентрация газа', 'gas_concentration', 'moles per liter', 'gas law', 'gas_density')
q44 = Question('Плотность воды', 'water_density', 'kg/m³', 'fluid mechanics', 'density_of_water')
q45 = Question('Вязкость', 'viscosity', 'pascal-seconds', 'fluid dynamics', 'fluid_resistance')
q46 = Question('Производная', 'derivative', 'unitless', 'calculus', 'rate_of_change')
q47 = Question('Интеграл', 'integral', 'unitless', 'calculus', 'total_sum')
q48 = Question('Момент инерции', 'moment_of_inertia', 'kg·m²', 'rotational dynamics', 'inertia_value')
q49 = Question('Сила тяжести', 'gravity_force', 'newtons', 'earth physics', 'gravitational_pull')
q50 = Question('Генерация энергии', 'energy_generation', 'kilowatts', 'power systems', 'energy_output')
q51 = Question('Коэффициент пропорциональности', 'proportionality_constant', 'unitless', 'mathematics', 'constant_value')
q52 = Question('Давление газа', 'gas_pressure', 'pascals', 'gas law', 'gas_pressure_value')
q53 = Question('Коэффициент трения', 'friction_coefficient', 'unitless', 'mechanics', 'friction_force')
q54 = Question('Объем жидкости', 'liquid_volume', 'liters', 'fluid mechanics', 'liquid_capacity')
q55 = Question('Конденсатор', 'capacitor', 'farads', 'electric circuits', 'capacitor_value')
q56 = Question('Частота колебаний', 'oscillation_frequency', 'hertz', 'waves', 'oscillation_rate')
q57 = Question('Молекулярное движение', 'molecular_motion', 'meters per second', 'thermodynamics', 'molecular_speed')
q58 = Question('Электрический заряд', 'electric_charge', 'coulombs', 'electricity', 'charge_amount')
q59 = Question('Радиус действия', 'range', 'meters', 'physics', 'action_radius')
q60 = Question('Момент импульса', 'angular_momentum', 'kg·m²/s', 'physics', 'rotational_momentum')
q61 = Question('Напряженность поля', 'field_intensity', 'volts per meter', 'electric field', 'field_strength')
q62 = Question('Эффективность устройства', 'device_efficiency', 'percentage', 'performance', 'operational_efficiency')
q63 = Question('Интервал времени', 'time_interval', 'seconds', 'time', 'elapsed_duration')
q64 = Question('Мощность системы', 'system_power', 'watts', 'energy system', 'power_output')
q65 = Question('Число Рейнольдса', 'Reynolds_number', 'unitless', 'fluid dynamics', 'flow_regime')
q66 = Question('Температурный режим', 'temperature_mode', 'Celsius', 'environment', 'temperature_setting')
q67 = Question('Показатель преломления', 'refractive_index', 'unitless', 'optics', 'light_refractive')
q68 = Question('Объем газа', 'gas_volume', 'liters', 'gas law', 'gas_capacity')
q69 = Question('Период колебаний', 'oscillation_period', 'seconds', 'wave motion', 'time_cycle')
q70 = Question('Энергия связи', 'binding_energy', 'electron volts', 'atomic physics', 'energy_bound')
q71 = Question('Нагрев', 'heating', 'watts', 'thermal dynamics', 'heat_generated')
q72 = Question('Угловая скорость', 'angular_velocity', 'radians per second', 'rotational motion', 'angular_speed')
q73 = Question('Температурная аномалия', 'temperature_anomaly', 'Celsius', 'climate science', 'temperature_variation')
q74 = Question('Загрязнение', 'pollution', 'ppm', 'environment', 'pollution_level')
q75 = Question('Реакция вещества', 'substance_reaction', 'rate per second', 'chemistry', 'reaction_speed')
q76 = Question('Физическая сила', 'physical_force', 'newtons', 'motion', 'force_exerted')
q77 = Question('Калорийность', 'caloric_value', 'calories', 'nutrition', 'food_energy')
q78 = Question('Углеродный след', 'carbon_footprint', 'kg CO2', 'environment', 'emission_amount')
q79 = Question('Площадь поверхности', 'surface_area', 'square meters', 'geometry', 'area_of_surface')
q80 = Question('Интенсивность света', 'light_intensity', 'lux', 'light', 'light_brightness')
q81 = Question('Напряжение в цепи', 'circuit_voltage', 'volts', 'electricity', 'voltage_drop')
q82 = Question('Кислотность', 'acidity', 'pH units', 'chemistry', 'acidity_level')
q83 = Question('Нахождение центра масс', 'center_of_mass', 'meters', 'physics', 'mass_center_location')
q84 = Question('Теплопроводность', 'thermal_conductivity', 'watts per meter per kelvin', 'material property', 'heat_transfer_coefficient')
q85 = Question('Диффузия', 'diffusion', 'meters squared per second', 'physics', 'diffusion_rate')
q86 = Question('Поглощение энергии', 'energy_absorption', 'joules', 'materials science', 'absorption_amount')
q87 = Question('Коэффициент теплоотдачи', 'heat_transfer_coefficient', 'watts per square meter per kelvin', 'thermodynamics', 'heat_transfer_value')
q88 = Question('Скорость звука в воздухе', 'speed_of_sound_air', 'meters per second', 'acoustics', 'sound_velocity')
q89 = Question('Коэффициент трения', 'friction_coefficient', 'dimensionless', 'mechanics', 'friction_factor')
q90 = Question('Молекулярная масса', 'molecular_mass', 'grams per mole', 'chemistry', 'molecular_weight')
q91 = Question('Температура плавления', 'melting_temperature', 'kelvins', 'materials_science', 'melting_point')
q92 = Question('Плотность вещества', 'substance_density', 'kilograms per cubic meter', 'physics', 'density')
q93 = Question('Теплота сгорания', 'heat_of_combustion', 'joules per gram', 'thermodynamics', 'combustion_energy')
q94 = Question('Энергия связи', 'binding_energy', 'joules', 'nuclear_physics', 'binding_energy_per_nucleon')
q95 = Question('Эффективность двигателя', 'engine_efficiency', 'percent', 'engineering', 'engine_performance')
q96 = Question('Коэффициент теплопроводности', 'thermal_conductivity', 'watts per meter per kelvin', 'materials_science', 'thermal_conductivity_value')
q97 = Question('Магнитная проницаемость', 'magnetic_permeability', 'henries per meter', 'electromagnetism', 'magnetic_permeability_value')
q88 = Question('Коэффициент трения', 'friction_coefficient', 'dimensionless', 'mechanics', 'friction_factor')
q89 = Question('Температура плавления', 'melting_temperature', 'kelvins', 'materials_science', 'melting_point')
q90 = Question('Молекулярная масса', 'molecular_mass', 'grams per mole', 'chemistry', 'molecular_weight')
q91 = Question('Плотность вещества', 'substance_density', 'kilograms per cubic meter', 'physics', 'density')
q92 = Question('Теплота сгорания', 'heat_of_combustion', 'joules per gram', 'thermodynamics', 'combustion_energy')
q93 = Question('Энергия связи', 'binding_energy', 'joules', 'nuclear_physics', 'binding_energy_per_nucleon')
q94 = Question('Эффективность двигателя', 'engine_efficiency', 'percent', 'engineering', 'engine_performance')
q95 = Question('Коэффициент теплопроводности', 'thermal_conductivity', 'watts per meter per kelvin', 'materials_science', 'thermal_conductivity_value')
q96 = Question('Магнитная проницаемость', 'magnetic_permeability', 'henries per meter', 'electromagnetism', 'magnetic_permeability_value')
q97 = Question('Электрическая проводимость', 'electrical_conductivity', 'siemens per meter', 'electromagnetism', 'electrical_conductivity_value')
q98 = Question('Сила тяжести', 'gravity_force', 'newtons', 'gravity', 'gravitational_force')
q99 = Question('Скорость света в вакууме', 'speed_of_light_vacuum', 'meters per second', 'physics', 'speed_of_light')
q100 = Question('Частота колебаний', 'vibration_frequency', 'hertz', 'acoustics', 'vibration_rate')
q101 = Question('Давление газа', 'gas_pressure', 'pascal', 'thermodynamics', 'gas_pressure_value')
q102 = Question('Электрический заряд', 'electric_charge', 'coulombs', 'electromagnetism', 'electric_charge_value')
q103 = Question('Площадь поверхности', 'surface_area', 'square meters', 'geometry', 'surface_area_value')
q104 = Question('Скорость потока жидкости', 'liquid_flow_speed', 'meters per second', 'fluid_dynamics', 'flow_speed')
q105 = Question('Теплопередача', 'heat_transfer', 'joules per second', 'thermodynamics', 'heat_flux')
q106 = Question('Сопротивление материала', 'material_resistance', 'ohms', 'electronics', 'resistance_value')
q107 = Question('Мощность источника', 'source_power', 'watts', 'electrical_engineering', 'power_output')
q108 = Question('Коэффициент полезного действия', 'efficiency_coefficient', 'percent', 'engineering', 'efficiency_factor')
q109 = Question('Скорость реакции', 'reaction_rate', 'moles per liter per second', 'chemistry', 'reaction_velocity')
q110 = Question('Время полураспада', 'half_life', 'seconds', 'nuclear_physics', 'radioactive_decay_time')
q111 = Question('Потери тепла', 'heat_loss', 'joules', 'thermodynamics', 'energy_dissipation')
q112 = Question('Температура кипения', 'boiling_temperature', 'kelvins', 'chemistry', 'boiling_point')
q113 = Question('Объем жидкости', 'liquid_volume', 'liters', 'fluid_dynamics', 'volume_of_liquid')
q114 = Question('Молекулярная структура', 'molecular_structure', 'description', 'chemistry', 'structure_type')
q115 = Question('Молекулярная форма', 'molecular_formula', 'chemical_formula', 'chemistry', 'chemical_composition')
q116 = Question('Давление на поверхности', 'surface_pressure', 'pascal', 'physics', 'pressure_at_surface')
q117 = Question('Амплитуда колебаний', 'vibration_amplitude', 'meters', 'acoustics', 'vibration_extent')
q118 = Question('Реактивный импульс', 'jet_impulse', 'newton-seconds', 'mechanical_engineering', 'impulse_value')
q119 = Question('Магнитная индукция', 'magnetic_induction', 'teslas', 'electromagnetism', 'magnetic_flux_density')
q120 = Question('Критическая температура', 'critical_temperature', 'kelvins', 'materials_science', 'critical_point')
q121 = Question('Инерция тела', 'body_inertia', 'kilogram meters squared', 'mechanics', 'inertia_value')
q122 = Question('Частота звука', 'sound_frequency', 'hertz', 'acoustics', 'sound_pitch')
q123 = Question('Прочность материала', 'material_strength', 'megapascals', 'materials_science', 'tensile_strength')
q124 = Question('Энергия фотона', 'photon_energy', 'joules', 'quantum_physics', 'photon_energy_value')
q125 = Question('Температура воды', 'water_temperature', 'celsius', 'environmental_science', 'water_temp')
q126 = Question('Скорость волны', 'wave_speed', 'meters per second', 'waves', 'wave_velocity')
q127 = Question('Коэффициент отражения', 'reflection_coefficient', 'dimensionless', 'optics', 'reflection_factor')
q128 = Question('Площадь круга', 'circle_area', 'square meters', 'geometry', 'circle_surface_area')
q129 = Question('Плотность воздуха', 'air_density', 'kilograms per cubic meter', 'atmospheric_science', 'air_density_value')
q130 = Question('Угол падения', 'angle_of_incidence', 'degrees', 'optics', 'incident_angle')
q131 = Question('Коэффициент преломления', 'refraction_coefficient', 'dimensionless', 'optics', 'refraction_index')
q132 = Question('Длительность колебаний', 'vibration_duration', 'seconds', 'acoustics', 'vibration_period')
q133 = Question('Электрическое поле', 'electric_field', 'volts per meter', 'electromagnetism', 'electric_field_strength')
q134 = Question('Теплоемкость вещества', 'specific_heat_capacity', 'joules per kilogram per kelvin', 'thermodynamics', 'specific_heat')
q135 = Question('Механическая энергия', 'mechanical_energy', 'joules', 'mechanics', 'kinetic_energy')
q136 = Question('Момент инерции', 'moment_of_inertia', 'kilogram meters squared', 'mechanics', 'rotational_inertia')
q137 = Question('Скорость осциллятора', 'oscillator_speed', 'meters per second', 'mechanics', 'oscillation_velocity')
q138 = Question('Энергия связи атома', 'atomic_binding_energy', 'joules', 'nuclear_physics', 'atomic_binding_energy_value')
q139 = Question('Тепловое расширение', 'thermal_expansion', 'per kelvin', 'materials_science', 'expansion_coefficient')
q140 = Question('Коэффициент передачи', 'transfer_coefficient', 'dimensionless', 'heat_transfer', 'thermal_transfer')
q141 = Question('Энергия на выходе', 'output_energy', 'joules', 'energy_systems', 'energy_output')
q142 = Question('Параметр активации', 'activation_parameter', 'energy', 'chemical_kinetics', 'activation_energy')
q143 = Question('Коэффициент теплопроводности воздуха', 'air_thermal_conductivity', 'watts per meter per kelvin', 'thermodynamics', 'air_conductivity')
q144 = Question('Площадь поверхности трения', 'friction_surface_area', 'square meters', 'mechanics', 'friction_surface')
q145 = Question('Скорость света в веществе', 'light_speed_in_material', 'meters per second', 'optics', 'light_velocity')
q146 = Question('Коэффициент расширения воды', 'water_expansion_coefficient', 'per kelvin', 'materials_science', 'water_expansion')
q147 = Question('Заряд на электрической пластине', 'charge_on_plate', 'coulombs', 'electrostatics', 'charge_value')
q148 = Question('Плотность нефти', 'oil_density', 'kilograms per cubic meter', 'geophysics', 'oil_density_value')
q149 = Question('Поглощение света', 'light_absorption', 'percent', 'optics', 'absorption_factor')
q150 = Question('Инерционная масса', 'inertial_mass', 'kilograms', 'mechanics', 'inertial_mass_value')
q151 = Question('Скорость электронов', 'electron_speed', 'meters per second', 'quantum_physics', 'electron_velocity')
q152 = Question('Энергия магнитного поля', 'magnetic_field_energy', 'joules', 'electromagnetism', 'magnetic_energy_value')
q153 = Question('Оптическая плотность', 'optical_density', 'dimensionless', 'optics', 'density_value')
q154 = Question('Проводимость воды', 'water_conductivity', 'siemens per meter', 'environmental_science', 'water_conductivity_value')
q155 = Question('Удельная плотность', 'specific_density', 'dimensionless', 'physics', 'specific_density_value')
q156 = Question('Температура звезды', 'star_temperature', 'kelvins', 'astronomy', 'star_temp')
q157 = Question('Эффективность трансформатора', 'transformer_efficiency', 'percent', 'electrical_engineering', 'transformer_performance')
q158 = Question('Количество молекул', 'molecule_count', 'molecules', 'chemistry', 'molecular_quantity')
q159 = Question('Сила магнитного поля', 'magnetic_field_strength', 'amperes per meter', 'electromagnetism', 'field_strength')
q160 = Question('Площадь солнечной панели', 'solar_panel_area', 'square meters', 'renewable_energy', 'solar_panel_surface')
q161 = Question('Мощность лазера', 'laser_power', 'watts', 'optics', 'laser_output')
q162 = Question('Теплотворная способность', 'calorific_value', 'joules per kilogram', 'energy', 'heat_capacity')
q163 = Question('Толщина слоя', 'layer_thickness', 'meters', 'materials_science', 'layer_thickness_value')
q164 = Question('Скорость роста растения', 'plant_growth_speed', 'centimeters per day', 'biology', 'growth_rate')
q165 = Question('Электрическое сопротивление воды', 'water_resistance', 'ohms', 'electrochemistry', 'water_resistance_value')
q166 = Question('Давление в трубопроводе', 'pipeline_pressure', 'pascal', 'fluid_dynamics', 'pipe_pressure')
q167 = Question('Площадь объекта', 'object_area', 'square meters', 'geometry', 'object_surface_area')
q168 = Question('Температура сгорания', 'combustion_temperature', 'kelvins', 'chemistry', 'burning_temp')
q169 = Question('Жёсткость материала', 'material_stiffness', 'newtons per meter', 'materials_science', 'material_hardness')
q170 = Question('Устойчивость к коррозии', 'corrosion_resistance', 'percent', 'materials_science', 'corrosion_resilience')
q171 = Question('Объём газа', 'gas_volume', 'cubic meters', 'gas_dynamics', 'gas_volume_value')
q172 = Question('Температура замерзания воды', 'freezing_temperature_water', 'kelvins', 'chemistry', 'freezing_point_water')
q173 = Question('Нагревательный коэффициент', 'heating_coefficient', 'watts per square meter per kelvin', 'thermodynamics', 'heating_rate')
q174 = Question('Теплотехническая мощность', 'thermal_power_capacity', 'watts', 'thermal_engineering', 'heat_capacity')
q175 = Question('Объём жидкости в сосуде', 'liquid_in_vessel_volume', 'liters', 'fluid_mechanics', 'liquid_volume_vessel')
q176 = Question('Электрическое напряжение', 'electric_voltage', 'volts', 'electrical_engineering', 'voltage_value')
q177 = Question('Скорость потока воздуха', 'air_flow_speed', 'meters per second', 'aerodynamics', 'air_flow_velocity')
q178 = Question('Угловая скорость', 'angular_velocity', 'radians per second', 'mechanics', 'angular_velocity_value')
q179 = Question('Теплопроводность материала', 'material_thermal_conductivity', 'watts per meter per kelvin', 'materials_science', 'thermal_conductivity_value')
q180 = Question('Удельная теплоемкость', 'specific_heat_capacity', 'joules per kilogram per kelvin', 'thermodynamics', 'specific_heat_value')
q181 = Question('Сопротивление провода', 'wire_resistance', 'ohms', 'electronics', 'resistance_wire')
q182 = Question('Скорость химической реакции', 'chemical_reaction_speed', 'moles per liter per second', 'chemistry', 'reaction_speed')
q183 = Question('Энергия химической связи', 'chemical_bond_energy', 'joules', 'chemistry', 'bond_energy')
q184 = Question('Температура кристаллизации', 'crystallization_temperature', 'kelvins', 'materials_science', 'crystallization_point')
q185 = Question('Скорость передачи данных', 'data_transfer_speed', 'bits per second', 'networking', 'transfer_speed')
q186 = Question('Сопротивление материала при температуре', 'material_resistance_at_temperature', 'ohms', 'thermodynamics', 'resistance_at_temp')
q187 = Question('Теплоотдача в веществе', 'heat_dissipation_in_substance', 'watts', 'thermodynamics', 'substance_heat_loss')
q188 = Question('Давление в атмосфере', 'atmospheric_pressure', 'pascal', 'meteorology', 'atmospheric_pressure_value')
q189 = Question('Электрическое поле вокруг заряда', 'electric_field_around_charge', 'volts per meter', 'electrostatics', 'field_strength_charge')
q190 = Question('Магнитный момент', 'magnetic_moment', 'ampere meters squared', 'electromagnetism', 'magnetic_moment_value')
q191 = Question('Эффективность солнечной панели', 'solar_panel_efficiency', 'percent', 'renewable_energy', 'solar_efficiency')
q192 = Question('Коэффициент отдачи двигателя', 'engine_thrust_coefficient', 'dimensionless', 'aerospace', 'engine_thrust_ratio')
q193 = Question('Коэффициент потерь тепла', 'heat_loss_coefficient', 'watts per meter squared per kelvin', 'thermodynamics', 'thermal_loss')
q194 = Question('Скорость химической реакции при повышении температуры', 'reaction_rate_temperature_effect', 'percent increase', 'chemistry', 'temperature_effect')
q195 = Question('Объём солнечной энергии', 'solar_energy_volume', 'joules', 'renewable_energy', 'solar_energy')
q196 = Question('Молекулярная масса воды', 'molecular_mass_water', 'grams per mole', 'chemistry', 'water_molecular_weight')
q197 = Question('Скорость вращения планеты', 'planet_rotation_speed', 'meters per second', 'astronomy', 'planetary_rotation')
q198 = Question('Радиус орбиты', 'orbital_radius', 'meters', 'astronomy', 'orbit_radius')
q199 = Question('Температура поверхности Луны', 'moon_surface_temperature', 'kelvins', 'astronomy', 'lunar_temperature')
q200 = Question('Электрический ток', 'electric_current', 'amperes', 'electrical_engineering', 'current_value')
q201 = Question('Удельная энергия аккумулятора', 'battery_energy_density', 'joules per kilogram', 'electrical_engineering', 'battery_energy')
q202 = Question('Скорость земного вращения', 'earth_rotation_speed', 'meters per second', 'geophysics', 'earth_rotational_velocity')
q203 = Question('Температура Земли на экваторе', 'earth_temperature_equator', 'celsius', 'geophysics', 'equatorial_temperature')
q204 = Question('Сила электромагнитного поля', 'electromagnetic_field_strength', 'amperes per meter', 'electromagnetism', 'field_strength')
q205 = Question('Давление на дне океана', 'ocean_floor_pressure', 'pascal', 'oceanography', 'deep_sea_pressure')
q206 = Question('Скорость ультразвука', 'ultrasonic_speed', 'meters per second', 'acoustics', 'ultrasound_velocity')
q207 = Question('Сила реактивной тяги', 'reaction_thrust_force', 'newtons', 'aerospace', 'thrust_force')
q208 = Question('Площадь поверхности Земли', 'earth_surface_area', 'square meters', 'geophysics', 'surface_area_earth')
q209 = Question('Скорость звука в воде', 'sound_speed_in_water', 'meters per second', 'acoustics', 'water_sound_velocity')
q210 = Question('Теплосодержание организма', 'body_heat_content', 'joules', 'biology', 'body_heat')
q211 = Question('Температура поверхности Солнца', 'sun_surface_temperature', 'kelvins', 'astronomy', 'solar_surface_temp')
q212 = Question('Количество кислорода в воздухе', 'oxygen_percentage_air', 'percent', 'environmental_science', 'oxygen_concentration')
q213 = Question('Сила вектора напряженности', 'electric_field_intensity', 'newtons per coulomb', 'electrostatics', 'field_intensity')
q214 = Question('Мощность ветра', 'wind_power', 'watts', 'renewable_energy', 'wind_power_value')
q215 = Question('Теплоемкость воды', 'water_heat_capacity', 'joules per liter per kelvin', 'thermodynamics', 'specific_heat_water')
q216 = Question('Длительность солнечного цикла', 'solar_cycle_duration', 'years', 'astronomy', 'sun_cycle')
q217 = Question('Скорость планетного ветра', 'solar_wind_speed', 'kilometers per second', 'space_science', 'solar_wind_velocity')
q218 = Question('Температура в центре Земли', 'core_temperature_earth', 'kelvins', 'geophysics', 'earth_core_temp')
q219 = Question('Мощность реактора', 'reactor_power', 'megawatts', 'nuclear_engineering', 'reactor_capacity')
q220 = Question('Электрическая проводимость материала', 'material_electrical_conductivity', 'siemens per meter', 'materials_science', 'conductivity_material')
q221 = Question('Сила напряжённого поля', 'tensile_field_strength', 'newtons', 'mechanical_engineering', 'tensile_strength')
q222 = Question('Объём ядра атома', 'atomic_core_volume', 'cubic meters', 'nuclear_physics', 'core_volume')
q223 = Question('Мощность двигателя внутреннего сгорания', 'internal_combustion_engine_power', 'horsepower', 'automotive_engineering', 'engine_power')
q224 = Question('Скорость химического разложения', 'chemical_decomposition_rate', 'moles per second', 'chemistry', 'decomposition_rate')
q225 = Question('Энергия диффузии', 'diffusion_energy', 'joules', 'physics', 'diffusion_energy_value')
q226 = Question('Температура ветряной турбины', 'wind_turbine_temperature', 'kelvins', 'renewable_energy', 'turbine_temperature')
q227 = Question('Теплообмен в жидкости', 'heat_exchange_in_liquid', 'watts', 'fluid_dynamics', 'liquid_heat_transfer')
q228 = Question('Энергия столкновения', 'collision_energy', 'joules', 'mechanics', 'collision_energy_value')
q229 = Question('Площадь контакта молекул', 'molecule_contact_area', 'square meters', 'materials_science', 'molecular_contact_area')
q230 = Question('Частота лазерного излучения', 'laser_emission_frequency', 'hertz', 'optics', 'laser_frequency')
q231 = Question('Давление газа при нагреве', 'gas_pressure_on_heating', 'pascal', 'gas_dynamics', 'pressure_on_heating')
q232 = Question('Энергия испарения воды', 'evaporation_energy_water', 'joules', 'chemistry', 'evaporation_energy')
q233 = Question('Магнитная индукция в проводнике', 'magnetic_induction_conductor', 'teslas', 'electromagnetism', 'magnetic_flux')
q234 = Question('Скорость вращения колеса', 'wheel_rotation_speed', 'radians per second', 'mechanical_engineering', 'wheel_rotation_velocity')
q235 = Question('Плотность стекла', 'glass_density', 'kilograms per cubic meter', 'materials_science', 'glass_density_value')
q236 = Question('Температура плавления металла', 'metal_melting_temperature', 'kelvins', 'materials_science', 'metal_melting_point')
q237 = Question('Скорость ускорения автомобиля', 'car_acceleration_speed', 'meters per second squared', 'automotive_engineering', 'acceleration_rate')
q238 = Question('Энергия фотосинтеза', 'photosynthesis_energy', 'joules', 'biology', 'photosynthesis_energy_value')
q239 = Question('Сила давления воды', 'water_pressure_force', 'newtons', 'hydrostatics', 'water_pressure_value')
q240 = Question('Температура плавления льда', 'ice_melting_temperature', 'kelvins', 'chemistry', 'ice_melting_point')
q241 = Question('Площадь поверхности звезды', 'star_surface_area', 'square meters', 'astronomy', 'star_surface')
q242 = Question('Сила сопротивления жидкости', 'liquid_resistance_force', 'newtons', 'fluid_dynamics', 'liquid_resistance')
q243 = Question('Молекулярная масса кислорода', 'molecular_mass_oxygen', 'grams per mole', 'chemistry', 'oxygen_molecular_weight')
q244 = Question('Температура замерзания нефти', 'oil_freezing_temperature', 'kelvins', 'chemistry', 'oil_freezing_point')
q245 = Question('Давление газа в сосуде', 'gas_pressure_in_container', 'pascal', 'gas_dynamics', 'gas_pressure_container')
q246 = Question('Энергия ионизации атома', 'atomic_ionization_energy', 'joules', 'quantum_physics', 'ionization_energy')
q247 = Question('Температура плавления золота', 'gold_melting_temperature', 'kelvins', 'materials_science', 'gold_melting_point')
q248 = Question('Молекулярная масса углекислого газа', 'molecular_mass_carbon_dioxide', 'grams per mole', 'chemistry', 'co2_molecular_weight')
q249 = Question('Площадь поверхности планеты', 'planet_surface_area', 'square meters', 'astronomy', 'planet_surface')
q250 = Question('Скорость светового потока', 'light_flux_speed', 'meters per second', 'optics', 'light_speed_flux')
q251 = Question('Температура озона', 'ozone_temperature', 'kelvins', 'environmental_science', 'ozone_temp')
q252 = Question('Давление жидкости в трубопроводе', 'liquid_pressure_in_pipeline', 'pascal', 'fluid_dynamics', 'liquid_pipeline_pressure')
q253 = Question('Магнитная восприимчивость вещества', 'material_magnetic_susceptibility', 'dimensionless', 'materials_science', 'magnetic_susceptibility')
q254 = Question('Скорость диффузии в жидкости', 'liquid_diffusion_speed', 'meters per second', 'chemistry', 'diffusion_velocity')
q255 = Question('Молекулярная масса аммиака', 'molecular_mass_ammonia', 'grams per mole', 'chemistry', 'ammonia_molecular_weight')
q256 = Question('Коэффициент теплопередачи', 'heat_transfer_coefficient', 'watts per meter squared per kelvin', 'thermal_dynamics', 'heat_transfer_value')
q257 = Question('Объём атмосферы Земли', 'earth_atmosphere_volume', 'cubic meters', 'geophysics', 'atmosphere_volume')
q258 = Question('Температура гидросферы', 'hydrosphere_temperature', 'kelvins', 'geophysics', 'water_temperature')
q259 = Question('Частота микроволн', 'microwave_frequency', 'hertz', 'electromagnetism', 'microwave_frequency_value')
q260 = Question('Скорость звуковых волн в воздухе', 'sound_speed_air', 'meters per second', 'acoustics', 'sound_velocity_air')
q261 = Question('Площадь атома', 'atom_surface_area', 'square meters', 'quantum_physics', 'atom_surface')
q262 = Question('Скорость электрона в проводнике', 'electron_speed_conductor', 'meters per second', 'electromagnetism', 'electron_velocity_conductor')
q263 = Question('Температура ядра Земли', 'earth_core_temperature', 'kelvins', 'geophysics', 'core_temperature')
q264 = Question('Скорость реакции окисления', 'oxidation_reaction_speed', 'moles per second', 'chemistry', 'oxidation_rate')
q265 = Question('Температура кипения воды на Эвересте', 'boiling_temperature_everest', 'kelvins', 'meteorology', 'boiling_point_everest')
q266 = Question('Радиус звезды', 'star_radius', 'meters', 'astronomy', 'star_radius_value')
q267 = Question('Мощность солнечного излучения', 'solar_radiation_power', 'watts per square meter', 'astronomy', 'solar_radiation')
q268 = Question('Температура проводника', 'conductor_temperature', 'kelvins', 'electrical_engineering', 'wire_temperature')
q269 = Question('Скорость распределения тепла', 'heat_distribution_speed', 'meters per second', 'thermodynamics', 'heat_flux_speed')
q270 = Question('Энергия резонанса', 'resonance_energy', 'joules', 'quantum_physics', 'resonance_energy_value')
q271 = Question('Давление воды на глубине', 'water_pressure_depth', 'pascal', 'oceanography', 'depth_water_pressure')
q272 = Question('Скорость изменения давления', 'pressure_change_speed', 'pascal per second', 'thermodynamics', 'pressure_rate')
q273 = Question('Магнитная чувствительность материала', 'material_magnetic_sensitivity', 'dimensionless', 'materials_science', 'magnetic_sensitivity')
q274 = Question('Температура атома', 'atom_temperature', 'kelvins', 'quantum_physics', 'atomic_temp')
q275 = Question('Энергия магнитного поля', 'magnetic_field_energy', 'joules', 'electromagnetism', 'field_energy')
q276 = Question('Площадь светового пятна', 'light_spot_area', 'square meters', 'optics', 'light_spot')
q277 = Question('Температура света', 'light_temperature', 'kelvins', 'optics', 'light_color_temperature')
q278 = Question('Скорость расширения Вселенной', 'universe_expansion_speed', 'kilometers per second', 'cosmology', 'expansion_rate')
q279 = Question('Коэффициент гигроскопичности', 'hygroscopic_coefficient', 'dimensionless', 'materials_science', 'hygroscopic_value')
q280 = Question('Магнитный поток', 'magnetic_flux', 'webers', 'electromagnetism', 'magnetic_flux_value')
q281 = Question('Давление на поверхности воды', 'water_surface_pressure', 'pascal', 'hydrostatics', 'surface_water_pressure')
q282 = Question('Коэффициент пульсации', 'pulsation_coefficient', 'dimensionless', 'acoustics', 'pulsation_index')
q283 = Question('Энергия фазового перехода', 'phase_transition_energy', 'joules', 'thermodynamics', 'transition_energy')
q284 = Question('Теплопроводность материала при низких температурах', 'thermal_conductivity_low_temp', 'watts per meter per kelvin', 'materials_science', 'low_temp_conductivity')
q285 = Question('Скорость светового потока в вакууме', 'vacuum_light_flux_speed', 'meters per second', 'optics', 'vacuum_light_speed')
q286 = Question('Температура магмы', 'magma_temperature', 'kelvins', 'geophysics', 'magma_temp')
q287 = Question('Площадь фокусного зеркала', 'focal_mirror_area', 'square meters', 'optics', 'mirror_area')
q288 = Question('Сила изменения магнитного поля', 'magnetic_field_change_force', 'newtons', 'electromagnetism', 'field_change_force')
q289 = Question('Температура горячего газа', 'hot_gas_temperature', 'kelvins', 'thermodynamics', 'gas_temperature')
q290 = Question('Энергия звуковых волн', 'sound_wave_energy', 'joules', 'acoustics', 'sound_energy')
q291 = Question('Скорость конвекции', 'convection_speed', 'meters per second', 'fluid_dynamics', 'convection_velocity')
q292 = Question('Теплосодержание организма человека', 'human_body_heat_content', 'joules', 'biology', 'human_heat')
q293 = Question('Площадь пересечения волны', 'wave_cross_section_area', 'square meters', 'wave_theory', 'wave_area')
q294 = Question('Коэффициент отражения', 'reflection_coefficient', 'dimensionless', 'optics', 'reflection_index')
q295 = Question('Энергия фотона', 'photon_energy', 'joules', 'quantum_physics', 'photon_energy_value')
q296 = Question('Скорость падения капли', 'drop_fall_speed', 'meters per second', 'fluid_dynamics', 'drop_velocity')
q297 = Question('Молекулярная масса угля', 'molecular_mass_coal', 'grams per mole', 'chemistry', 'coal_molecular_weight')
q298 = Question('Давление в системе охлаждения', 'cooling_system_pressure', 'pascal', 'mechanical_engineering', 'cooling_pressure')
q299 = Question('Температура альбедо поверхности', 'surface_albedo_temperature', 'kelvins', 'astronomy', 'surface_albedo_temp')
q300 = Question('Энергия рассеяния', 'scattering_energy', 'joules', 'physics', 'scattering_energy_value')
q301 = Question('Скорость машины', 'car_speed', 'meters per second', 'automotive', 'car_velocity')
q302 = Question('Температура воды', 'water_temperature', 'kelvins', 'environment', 'water_temp')
q303 = Question('Давление в шинах', 'tire_pressure', 'pascal', 'automotive', 'tire_pressure_value')
q304 = Question('Длина волны', 'wavelength', 'meters', 'physics', 'wave_length')
q305 = Question('Площадь окна', 'window_area', 'square meters', 'construction', 'window_surface')
q306 = Question('Масса воздуха', 'air_mass', 'kilograms', 'atmosphere', 'air_weight')
q307 = Question('Энергия воды', 'water_energy', 'joules', 'hydropower', 'water_energy_value')
q308 = Question('Плотность металла', 'metal_density', 'kilograms per cubic meter', 'materials', 'metal_density_value')
q309 = Question('Частота звука', 'sound_frequency', 'hertz', 'acoustics', 'sound_freq')
q310 = Question('Глубина океана', 'ocean_depth', 'meters', 'geography', 'depth_ocean')
q311 = Question('Молекулярная масса воды', 'water_molecular_weight', 'grams per mole', 'chemistry', 'water_mol_weight')
q312 = Question('Кислотность почвы', 'soil_acidity', 'pH', 'agriculture', 'soil_acid')
q313 = Question('Мощность генератора', 'generator_power', 'watts', 'electrical', 'gen_power')
q314 = Question('Скорость ветра', 'wind_speed', 'meters per second', 'meteorology', 'wind_velocity')
q315 = Question('Площадь участка земли', 'land_area', 'square meters', 'geography', 'land_surface')
q316 = Question('Температура солнечного света', 'sunlight_temperature', 'kelvins', 'astronomy', 'sunlight_temp')
q317 = Question('Мощность лазера', 'laser_power', 'watts', 'optics', 'laser_strength')
q318 = Question('Сила удара', 'impact_force', 'newtons', 'physics', 'impact_strength')
q319 = Question('Энергия света', 'light_energy', 'joules', 'optics', 'light_power')
q320 = Question('Площадь крыши', 'roof_area', 'square meters', 'construction', 'roof_surface')
q321 = Question('Скорость течения реки', 'river_speed', 'meters per second', 'hydrology', 'river_velocity')
q322 = Question('Мощность двигателя', 'engine_power', 'horsepower', 'automotive', 'motor_power')
q323 = Question('Энергия удара', 'impact_energy', 'joules', 'physics', 'impact_energy_value')
q324 = Question('Температура в космосе', 'space_temperature', 'kelvins', 'astronomy', 'space_temp')
q325 = Question('Давление воздуха в баллоне', 'air_pressure_bottle', 'pascal', 'physics', 'bottle_pressure')
q326 = Question('Площадь комнаты', 'room_area', 'square meters', 'architecture', 'room_surface')
q327 = Question('Скорость света в воде', 'light_speed_in_water', 'meters per second', 'optics', 'water_light_speed')
q328 = Question('Глубина прудa', 'pond_depth', 'meters', 'geography', 'pond_depth_value')
q329 = Question('Температура замерзания воды', 'water_freezing_point', 'kelvins', 'chemistry', 'water_freeze_temp')
q330 = Question('Энергия химической реакции', 'chemical_reaction_energy', 'joules', 'chemistry', 'reaction_energy')
q331 = Question('Плотность льда', 'ice_density', 'kilograms per cubic meter', 'chemistry', 'ice_density_value')
q332 = Question('Скорость роста растения', 'plant_growth_speed', 'centimeters per day', 'biology', 'plant_growth')
q333 = Question('Мощность аккумулятора', 'battery_power', 'watts', 'electronics', 'battery_strength')
q334 = Question('Скорость теплопередачи', 'heat_transfer_speed', 'watts per meter squared', 'thermodynamics', 'heat_transfer_rate')
q335 = Question('Энергия изменения температуры', 'temperature_change_energy', 'joules', 'thermodynamics', 'temp_change_energy')
q336 = Question('Площадь огорода', 'garden_area', 'square meters', 'agriculture', 'garden_surface')
q337 = Question('Температура двигателя', 'engine_temperature', 'kelvins', 'automotive', 'motor_temperature')
q338 = Question('Скорость восстановления леса', 'forest_regrowth_speed', 'meters per year', 'ecology', 'forest_regrowth')
q339 = Question('Масса океана', 'ocean_mass', 'kilograms', 'geophysics', 'ocean_weight')
q340 = Question('Энергия ветра', 'wind_energy', 'joules', 'renewable_energy', 'wind_power')
q341 = Question('Скорость пешехода', 'walking_speed', 'meters per second', 'sports', 'walking_velocity')
q342 = Question('Температура льда', 'ice_temperature', 'kelvins', 'chemistry', 'ice_temp')
q343 = Question('Площадь автомобильного стекла', 'car_window_area', 'square meters', 'automotive', 'window_area_value')
q344 = Question('Скорость работы компьютера', 'computer_speed', 'ghz', 'computing', 'computer_clock_speed')
q345 = Question('Давление газа в сосуде', 'gas_pressure_vessel', 'pascal', 'physics', 'vessel_gas_pressure')
q346 = Question('Энергия сжатого воздуха', 'compressed_air_energy', 'joules', 'engineering', 'compressed_air_power')
q347 = Question('Температура воды в реке', 'river_water_temperature', 'kelvins', 'hydrology', 'river_temp')
q348 = Question('Скорость роста бактерий', 'bacteria_growth_speed', 'micrometers per hour', 'biology', 'bacteria_growth')
q349 = Question('Площадь поля', 'field_area', 'square meters', 'agriculture', 'field_surface')
q350 = Question('Молекулярная масса углерода', 'carbon_molecular_weight', 'grams per mole', 'chemistry', 'carbon_weight')
q351 = Question('Температура внутри холодильника', 'fridge_temperature', 'kelvins', 'home_appliances', 'fridge_temp')
q352 = Question('Скорость изменения температуры', 'temperature_change_speed', 'kelvins per second', 'thermodynamics', 'temperature_rate')
q353 = Question('Площадь детского сада', 'kindergarten_area', 'square meters', 'education', 'kindergarten_surface')
q354 = Question('Мощность солнечных панелей', 'solar_panel_power', 'watts', 'renewable_energy', 'solar_panel_strength')
q355 = Question('Скорость передачи данных', 'data_transfer_speed', 'megabits per second', 'networking', 'data_speed')
q356 = Question('Глубина колодца', 'well_depth', 'meters', 'geography', 'well_depth_value')
q357 = Question('Энергия атомного ядра', 'atomic_core_energy', 'joules', 'nuclear_physics', 'core_energy')
q358 = Question('Скорость света в вакууме', 'speed_of_light_in_vacuum', 'meters per second', 'physics', 'light_speed_vacuum')
q359 = Question('Температура плавления меди', 'copper_melting_point', 'kelvins', 'materials', 'copper_melting')
q360 = Question('Мощность радиостанции', 'radio_station_power', 'watts', 'electronics', 'radio_power')
q361 = Question('Скорость окисления', 'oxidation_speed', 'moles per second', 'chemistry', 'oxidation_rate_value')
q362 = Question('Температура электропечи', 'electric_furnace_temperature', 'kelvins', 'metallurgy', 'furnace_temp')
q363 = Question('Сила тяжести на Луне', 'moon_gravity', 'newtons', 'astronomy', 'moon_gravity_value')
q364 = Question('Энергия механического движения', 'mechanical_motion_energy', 'joules', 'mechanics', 'motion_energy')
q365 = Question('Скорость оседания пыли', 'dust_settlement_speed', 'meters per second', 'environment', 'dust_fall_rate')
q366 = Question('Давление в камере сгорания', 'combustion_chamber_pressure', 'pascal', 'engineering', 'chamber_pressure')
q367 = Question('Площадь бассейна', 'pool_area', 'square meters', 'construction', 'pool_surface')
q368 = Question('Температура жаркой поверхности', 'hot_surface_temperature', 'kelvins', 'engineering', 'hot_surface_temp')
q369 = Question('Скорость вращения колеса', 'wheel_rotation_speed', 'radians per second', 'mechanical_engineering', 'wheel_rotational_speed')
q370 = Question('Мощность двигателя реактивного самолета', 'jet_engine_power', 'kilonewtons', 'aerospace', 'jet_power')
q371 = Question('Энергия фотосинтеза', 'photosynthesis_energy', 'joules', 'biology', 'photosynthesis_energy_value')
q372 = Question('Площадь танка', 'tank_area', 'square meters', 'military', 'tank_surface')
q373 = Question('Скорость падения предмета', 'falling_speed', 'meters per second', 'physics', 'fall_velocity')
q374 = Question('Энергия электрического тока', 'electric_current_energy', 'joules', 'electrical_engineering', 'current_energy')
q375 = Question('Скорость осмоса', 'osmosis_speed', 'meters per second', 'biology', 'osmosis_rate')
q376 = Question('Температура горячей жидкости', 'hot_liquid_temperature', 'kelvins', 'chemistry', 'hot_liquid_temp')
q377 = Question('Давление на дне океана', 'ocean_floor_pressure', 'pascal', 'geophysics', 'floor_pressure')
q378 = Question('Энергия солнечного излучения', 'solar_radiation_energy', 'joules', 'solar_energy', 'solar_radiation_value')
q379 = Question('Скорость протекания реакции', 'reaction_speed', 'moles per second', 'chemistry', 'reaction_rate')
q380 = Question('Сила магнитного поля', 'magnetic_field_strength', 'teslas', 'electromagnetism', 'field_strength')
q381 = Question('Площадь кухни', 'kitchen_area', 'square meters', 'architecture', 'kitchen_surface')
q382 = Question('Скорость корабля', 'ship_speed', 'meters per second', 'nautical', 'ship_velocity')
q383 = Question('Температура льда в холодильнике', 'freezer_ice_temperature', 'kelvins', 'home_appliances', 'freezer_ice_temp')
q384 = Question('Скорость роста бактерий в воде', 'bacteria_growth_in_water_speed', 'micrometers per hour', 'biology', 'bacteria_water_growth')
q385 = Question('Давление в капсуле', 'capsule_pressure', 'pascal', 'space', 'capsule_pressure_value')
q386 = Question('Температура в центре Земли', 'earth_core_temperature', 'kelvins', 'geophysics', 'core_temperature')
q387 = Question('Мощность атомного реактора', 'nuclear_reactor_power', 'megawatts', 'nuclear_physics', 'reactor_power')
q388 = Question('Скорость вращения Земли', 'earth_rotation_speed', 'meters per second', 'astronomy', 'earth_rotation_velocity')
q389 = Question('Сила реакции', 'reaction_force', 'newtons', 'physics', 'reaction_strength')
q390 = Question('Молекулярная масса кислорода', 'oxygen_molecular_weight', 'grams per mole', 'chemistry', 'oxygen_weight')
q391 = Question('Температура на поверхности Марса', 'mars_surface_temperature', 'kelvins', 'astronomy', 'mars_temp')
q392 = Question('Скорость звука в воде', 'sound_speed_in_water', 'meters per second', 'acoustics', 'water_sound_velocity')
q393 = Question('Мощность электроэнергии', 'electric_power', 'watts', 'electrical', 'power_output')
q394 = Question('Давление в твердом теле', 'solid_body_pressure', 'pascal', 'solid_state_physics', 'solid_pressure')
q395 = Question('Температура плавления железа', 'iron_melting_point', 'kelvins', 'materials', 'iron_melting_temp')
q396 = Question('Скорость старения', 'aging_speed', 'years per decade', 'biology', 'aging_rate')
q397 = Question('Сила тяжести на Земле', 'earth_gravity', 'newtons', 'geophysics', 'earth_gravity_value')
q398 = Question('Температура жидкости в печи', 'liquid_furnace_temperature', 'kelvins', 'metallurgy', 'furnace_liquid_temp')
q399 = Question('Молекулярная масса аммиака', 'ammonia_molecular_weight', 'grams per mole', 'chemistry', 'ammonia_mol_weight')
q400 = Question('Скорость волны в воде', 'wave_speed_in_water', 'meters per second', 'fluid_dynamics', 'water_wave_speed')
q401 = Question('Температура вулкана', 'volcano_temperature', 'kelvins', 'geophysics', 'volcano_temp')
q402 = Question('Энергия газа', 'gas_energy', 'joules', 'thermodynamics', 'gas_energy_value')
q403 = Question('Площадь поля для гольфа', 'golf_field_area', 'square meters', 'sports', 'golf_field_surface')
q404 = Question('Скорость протекания жидкости', 'liquid_flow_speed', 'meters per second', 'fluid_dynamics', 'liquid_flow_velocity')
q405 = Question('Мощность ветровой турбины', 'wind_turbine_power', 'kilowatts', 'renewable_energy', 'turbine_power')
q406 = Question('Давление в вакууме', 'vacuum_pressure', 'pascal', 'physics', 'vacuum_pressure_value')
q407 = Question('Температура поверхности Луны', 'moon_surface_temperature', 'kelvins', 'astronomy', 'moon_temp')
q408 = Question('Масса электрического заряда', 'electric_charge_mass', 'grams', 'electrical', 'charge_mass')
q409 = Question('Скорость распространения света', 'light_propagation_speed', 'meters per second', 'optics', 'light_speed')
q410 = Question('Площадь картонной коробки', 'cardboard_box_area', 'square meters', 'manufacturing', 'box_surface')
q411 = Question('Мощность солнечной батареи', 'solar_battery_power', 'watts', 'solar_energy', 'solar_battery_power')
q412 = Question('Скорость осмотического давления', 'osmotic_pressure_speed', 'meters per second', 'biology', 'osmotic_pressure')
q413 = Question('Температура воды в океане', 'ocean_water_temperature', 'kelvins', 'hydrology', 'ocean_temp')
q414 = Question('Сила магнитного поля Земли', 'earth_magnetic_field_strength', 'teslas', 'geophysics', 'earth_magnetic_field')
q415 = Question('Молекулярная масса азота', 'nitrogen_molecular_weight', 'grams per mole', 'chemistry', 'nitrogen_weight')
q416 = Question('Энергия магнитного поля', 'magnetic_field_energy', 'joules', 'electromagnetism', 'field_energy')
q417 = Question('Скорость роста деревьев', 'tree_growth_speed', 'centimeters per year', 'ecology', 'tree_growth')
q418 = Question('Температура в котле', 'boiler_temperature', 'kelvins', 'engineering', 'boiler_temp')
q419 = Question('Мощность электрического мотора', 'electric_motor_power', 'watts', 'electronics', 'motor_power')
q420 = Question('Скорость возникновения давления', 'pressure_build_speed', 'pascal per second', 'physics', 'pressure_build_rate')
q421 = Question('Площадь детской площадки', 'playground_area', 'square meters', 'construction', 'playground_surface')
q422 = Question('Энергия солнечного света', 'solar_light_energy', 'joules', 'solar_energy', 'sunlight_energy')
q423 = Question('Скорость вращения колесика мыши', 'mouse_wheel_rotation_speed', 'radians per second', 'electronics', 'mouse_wheel_speed')
q424 = Question('Давление воздуха в горах', 'mountain_air_pressure', 'pascal', 'geophysics', 'mountain_pressure')
q425 = Question('Температура в пустыне', 'desert_temperature', 'kelvins', 'geography', 'desert_temp')
q426 = Question('Скорость света в стекле', 'light_speed_in_glass', 'meters per second', 'optics', 'glass_light_speed')
q427 = Question('Энергия атома', 'atom_energy', 'joules', 'atomic_physics', 'atomic_energy_value')
q428 = Question('Молекулярная масса метана', 'methane_molecular_weight', 'grams per mole', 'chemistry', 'methane_weight')
q429 = Question('Скорость эволюции', 'evolution_speed', 'years per species', 'biology', 'evolution_rate')
q430 = Question('Температура в разогретом воздухе', 'heated_air_temperature', 'kelvins', 'physics', 'heated_air_temp')
q431 = Question('Скорость звука в газе', 'sound_speed_in_gas', 'meters per second', 'acoustics', 'gas_sound_speed')
q432 = Question('Мощность трансформатора', 'transformer_power', 'kilowatts', 'electronics', 'transformer_strength')
q433 = Question('Сила тока', 'electric_current_strength', 'amperes', 'electrical', 'current_strength')
q434 = Question('Температура твердого тела', 'solid_body_temperature', 'kelvins', 'solid_state_physics', 'solid_temp')
q435 = Question('Скорость работы процессора', 'processor_speed', 'ghz', 'computing', 'cpu_speed')
q436 = Question('Молекулярная масса серы', 'sulfur_molecular_weight', 'grams per mole', 'chemistry', 'sulfur_weight')
q437 = Question('Энергия атомного взаимодействия', 'atomic_interaction_energy', 'joules', 'nuclear_physics', 'atomic_interaction_value')
q438 = Question('Скорость химической реакции', 'chemical_reaction_speed', 'moles per second', 'chemistry', 'reaction_speed')
q439 = Question('Температура на поверхности Венеры', 'venus_surface_temperature', 'kelvins', 'astronomy', 'venus_temp')
q440 = Question('Скорость роста грибов', 'fungus_growth_speed', 'millimeters per day', 'biology', 'fungus_growth')
q441 = Question('Энергия реакции с кислородом', 'oxygen_reaction_energy', 'joules', 'chemistry', 'oxygen_reaction_value')
q442 = Question('Температура электродов в батарее', 'battery_electrode_temperature', 'kelvins', 'electronics', 'battery_electrode_temp')
q443 = Question('Скорость обмена веществ', 'metabolism_speed', 'calories per hour', 'biology', 'metabolism_rate')
q444 = Question('Мощность электростанции', 'power_plant_power', 'megawatts', 'energy', 'plant_power')
q445 = Question('Давление в шарике', 'ball_pressure', 'pascal', 'physics', 'ball_pressure_value')
q446 = Question('Температура на поверхности Юпитера', 'jupiter_surface_temperature', 'kelvins', 'astronomy', 'jupiter_temp')
q447 = Question('Скорость роста кристаллов', 'crystal_growth_speed', 'micrometers per hour', 'chemistry', 'crystal_growth_rate')
q448 = Question('Энергия электрического поля', 'electric_field_energy', 'joules', 'electromagnetism', 'electric_field_value')
q449 = Question('Молекулярная масса углекислого газа', 'carbon_dioxide_molecular_weight', 'grams per mole', 'chemistry', 'co2_weight')
q450 = Question('Температура на поверхности Земли', 'earth_surface_temperature', 'kelvins', 'geophysics', 'earth_surface_temp')
q451 = Question('Скорость изменений климата', 'climate_change_speed', 'degrees per century', 'geography', 'climate_change_rate')
q452 = Question('Мощность газовой плиты', 'gas_stove_power', 'watts', 'appliances', 'stove_power')
q453 = Question('Температура на глубине океана', 'ocean_depth_temperature', 'kelvins', 'geophysics', 'depth_ocean_temp')
q454 = Question('Скорость диффузии', 'diffusion_speed', 'meters per second', 'physics', 'diffusion_rate')
q455 = Question('Мощность ветра', 'wind_power', 'watts', 'meteorology', 'wind_energy')
q456 = Question('Температура расплавленного металла', 'molten_metal_temperature', 'kelvins', 'materials', 'molten_metal_temp')
q457 = Question('Скорость воды в реке', 'river_water_speed', 'meters per second', 'hydrology', 'river_water_velocity')
q458 = Question('Энергия химической реакции', 'chemical_reaction_energy', 'joules', 'chemistry', 'chemical_energy')
q459 = Question('Температура на Марсе', 'mars_temperature', 'kelvins', 'astronomy', 'mars_surface_temp')
q460 = Question('Скорость света в воде', 'light_speed_in_water', 'meters per second', 'optics', 'water_light_speed')
q461 = Question('Мощность парового котла', 'steam_boiler_power', 'watts', 'engineering', 'boiler_power')
q462 = Question('Давление на поверхности Луны', 'moon_surface_pressure', 'pascal', 'geophysics', 'moon_pressure')
q463 = Question('Температура воздуха в тропиках', 'tropical_air_temperature', 'kelvins', 'climate', 'tropical_air_temp')
q464 = Question('Скорость обмена кислорода в клетках', 'oxygen_cell_exchange_speed', 'milligrams per second', 'biology', 'oxygen_exchange_rate')
q465 = Question('Мощность лазера', 'laser_power', 'watts', 'optics', 'laser_strength')
q466 = Question('Температура поверхности воды', 'water_surface_temperature', 'kelvins', 'hydrology', 'water_temp')
q467 = Question('Скорость роста бактерий', 'bacteria_growth_speed', 'centimeters per day', 'biology', 'bacteria_growth_rate')
q468 = Question('Энергия давления', 'pressure_energy', 'joules', 'physics', 'pressure_energy_value')
q469 = Question('Температура вакуума', 'vacuum_temperature', 'kelvins', 'physics', 'vacuum_temp')
q470 = Question('Мощность тормозной системы', 'braking_system_power', 'watts', 'mechanical_engineering', 'braking_power')
q471 = Question('Скорость планет в солнечной системе', 'planet_orbit_speed', 'kilometers per second', 'astronomy', 'planet_velocity')
q472 = Question('Энергия давления газа', 'gas_pressure_energy', 'joules', 'thermodynamics', 'gas_pressure_value')
q473 = Question('Температура в котле парового двигателя', 'steam_engine_boiler_temperature', 'kelvins', 'engineering', 'steam_engine_boiler_temp')
q474 = Question('Мощность холодильника', 'refrigerator_power', 'watts', 'appliances', 'fridge_power')
q475 = Question('Скорость вспышки молнии', 'lightning_strike_speed', 'meters per second', 'meteorology', 'lightning_speed')
q476 = Question('Температура в свете лампы', 'light_bulb_temperature', 'kelvins', 'electronics', 'bulb_temp')
q477 = Question('Скорость осциллятора', 'oscillator_speed', 'hertz', 'electronics', 'oscillator_frequency')
q478 = Question('Энергия при столкновении', 'collision_energy', 'joules', 'mechanics', 'collision_energy_value')
q479 = Question('Температура в космосе', 'space_temperature', 'kelvins', 'astronomy', 'space_temp')
q480 = Question('Скорость снаряда', 'projectile_speed', 'meters per second', 'mechanics', 'projectile_velocity')
q481 = Question('Мощность генератора', 'generator_power', 'watts', 'engineering', 'generator_strength')
q482 = Question('Температура в печи для выпечки', 'baking_oven_temperature', 'kelvins', 'appliances', 'oven_temp')
q483 = Question('Скорость отклика системы', 'system_response_time', 'milliseconds', 'computing', 'system_latency')
q484 = Question('Энергия поля магнитного резонанса', 'magnetic_resonance_field_energy', 'joules', 'medical_physics', 'mri_field_energy')
q485 = Question('Температура в сверхпроводнике', 'superconductor_temperature', 'kelvins', 'solid_state_physics', 'superconductor_temp')
q486 = Question('Скорость восстановления энергии', 'energy_recovery_speed', 'joules per second', 'energy', 'energy_recovery_rate')
q487 = Question('Мощность супермаркета', 'supermarket_power', 'watts', 'retail', 'supermarket_power_value')
q488 = Question('Температура в холодильной камере', 'freezer_temperature', 'kelvins', 'appliances', 'freezer_temp')
q489 = Question('Скорость роста растений', 'plant_growth_speed', 'centimeters per week', 'biology', 'plant_growth_rate')
q490 = Question('Энергия химического элемента', 'chemical_element_energy', 'joules', 'chemistry', 'element_energy_value')
q491 = Question('Температура в холодильнике', 'fridge_temperature', 'kelvins', 'appliances', 'fridge_temp')
q492 = Question('Скорость распространения волн', 'wave_propagation_speed', 'meters per second', 'physics', 'wave_speed')
q493 = Question('Мощность солнечной панели', 'solar_panel_power', 'watts', 'solar_energy', 'panel_power')
q494 = Question('Температура в камере сгорания', 'combustion_chamber_temperature', 'kelvins', 'engineering', 'combustion_temp')
q495 = Question('Скорость химического разложения', 'chemical_decomposition_speed', 'moles per second', 'chemistry', 'decomposition_speed')
q496 = Question('Энергия молекул', 'molecular_energy', 'joules', 'chemistry', 'molecule_energy_value')
q497 = Question('Температура воздуха в горах', 'mountain_air_temperature', 'kelvins', 'geophysics', 'mountain_air_temp')
q498 = Question('Скорость течения реки', 'river_current_speed', 'meters per second', 'hydrology', 'river_current_velocity')
q499 = Question('Энергия кристаллов', 'crystal_energy', 'joules', 'chemistry', 'crystal_energy_value')
q500 = Question('Скорость света в вакууме', 'vacuum_light_speed', 'meters per second', 'optics', 'vacuum_light_speed_value')





radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, 
    q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
    q21, q22, q23, q24, q25, q26, q27, q28, q29, q30,
    q31, q32, q33, q34, q35, q36, q37, q38, q39, q40,
    q41, q42, q43, q44, q45, q46, q47, q48, q49, q50,
    q51, q52, q53, q54, q55, q56, q57, q58, q59, q60,
    q61, q62, q63, q64, q65, q66, q67, q68, q69, q70,
    q71, q72, q73, q74, q75, q76, q77, q78, q79, q80,
    q81, q82, q83, q84, q85, q86, q87, q88, q89, q90,
    q91, q92, q93, q94, q95, q96, q97, q98, q99, q100,
    q101, q102, q103, q104, q105, q106, q107, q108, q109, q110,
    q111, q112, q113, q114, q115, q116, q117, q118, q119, q120,
    q121, q122, q123, q124, q125, q126, q127, q128, q129, q130,
    q131, q132, q133, q134, q135, q136, q137, q138, q139, q140,
    q141, q142, q143, q144, q145, q146, q147, q148, q149, q150,
    q151, q152, q153, q154, q155, q156, q157, q158, q159, q160,
    q161, q162, q163, q164, q165, q166, q167, q168, q169, q170,
    q171, q172, q173, q174, q175, q176, q177, q178, q179, q180,
    q181, q182, q183, q184, q185, q186, q187, q188, q189, q190,
    q191, q192, q193, q194, q195, q196, q197, q198, q199, q200,
    q201, q202, q203, q204, q205, q206, q207, q208, q209, q210,
    q211, q212, q213, q214, q215, q216, q217, q218, q219, q220,
    q221, q222, q223, q224, q225, q226, q227, q228, q229, q230,
    q231, q232, q233, q234, q235, q236, q237, q238, q239, q240,
    q241, q242, q243, q244, q245, q246, q247, q248, q249, q250,
    q251, q252, q253, q254, q255, q256, q257, q258, q259, q260,
    q261, q262, q263, q264, q265, q266, q267, q268, q269, q270,
    q271, q272, q273, q274, q275, q276, q277, q278, q279, q280,
    q281, q282, q283, q284, q285, q286, q287, q288, q289, q290,
    q291, q292, q293, q294, q295, q296, q297, q298, q299, q300,
    q301, q302, q303, q304, q305, q306, q307, q308, q309, q310,
    q311, q312, q313, q314, q315, q316, q317, q318, q319, q320,
    q321, q322, q323, q324, q325, q326, q327, q328, q329, q330,
    q331, q332, q333, q334, q335, q336, q337, q338, q339, q340,
    q341, q342, q343, q344, q345, q346, q347, q348, q349, q350,
    q351, q352, q353, q354, q355, q356, q357, q358, q359, q360,
    q361, q362, q363, q364, q365, q366, q367, q368, q369, q370,
    q371, q372, q373, q374, q375, q376, q377, q378, q379, q380,
    q381, q382, q383, q384, q385, q386, q387, q388, q389, q390,
    q391, q392, q393, q394, q395, q396, q397, q398, q399, q400,
    q401, q402, q403, q404, q405, q406, q407, q408, q409, q410,
    q411, q412, q413, q414, q415, q416, q417, q418, q419, q420,
    q421, q422, q423, q424, q425, q426, q427, q428, q429, q430,
    q431, q432, q433, q434, q435, q436, q437, q438, q439, q440,
    q441, q442, q443, q444, q445, q446, q447, q448, q449, q450,
    q451, q452, q453, q454, q455, q456, q457, q458, q459, q460,
    q461, q462, q463, q464, q465, q466, q467, q468, q469, q470,
    q471, q472, q473, q474, q475, q476, q477, q478, q479, q480,
    q481, q482, q483, q484, q485, q486, q487, q488, q489, q490,
    q491, q492, q493, q494, q495, q496, q497, q498, q499, q500
]




def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)

    answers = [cur_q.answer, cur_q.wrong_answer1, cur_q.wrong_answer2, cur_q.wrong_answer3]
    shuffle(answers)

    for btn, text in zip(radio_buttons, answers):
        btn.setText(text)

new_question()
show_question()
btn_ok.clicked.connect(click_OK)

def rest():
    win_card.hide()
    n = btn_minutes.value() * 60
    sleep(n)
    win_card.show()

btn_sleep.clicked.connect(rest)

def show_menu():
    win_card.hide()
    menu_win.show()

btn_menu.clicked.connect(show_menu) 

def hide_menu():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(hide_menu)









def clear():   
    line_quest.clear()
    line_right_ans.clear()
    line_wrong1_ans.clear()
    line_wrong2_ans.clear()
    line_wrong3_ans.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(line_quest.text(), line_right_ans.text(), 
                     line_wrong1_ans.text(), line_wrong2_ans.text(), line_wrong3_ans.text())
    questions.append(new_q)
    clear()

btn_add_quest.clicked.connect(add_question)

def stat_generator():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right / cur_q.count_ask) * 100

    text = f'Разів відповіли: {cur_q.count_ask}\n' \
           f'Вірних відповідей: {cur_q.count_right}\n' \
           f'Успішність: {round(c, 2)}%'
    
    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()

btn_menu.clicked.connect(stat_generator)

app.exec_()
