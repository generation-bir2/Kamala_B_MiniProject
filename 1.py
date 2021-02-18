
/*Complete School Management system Database*/

create table public.tbl_Schoo(sch_id serial primary key,
							sch_name varchar(40) not null,
							sch_address varchar(50)not null,
							sch_phone_no integer unique)
							
create table public.tbl_student(st_id serial primary key,
							 roll_no integer unique,
							st_name varchar(40)not null,
							pa_id integer not null ,    /*FK*/
							reg_id integer not null, /*FK*/
							st_phone_no integer unique,
							st_DOB date not null,
							st_gender varchar(10)not null,
							st_email varchar(40)unique,
								constraint parient_id foreign key(pa_id) references tbl_parient(pa_id),
								constraint registration_id foreign key(reg_id) references public.tbl_registration(reg_id)
							)	
create table public.tbl_parient(pa_id serial primary key,
							 pa_name varchar(40)not null,
							pa_phone_no integer unique,
							Pa_occupation varchar(30)not null
							)	
create table public.tbl_registration(reg_id serial primary key,
									 reg_no integer not null,
									reg_date date not null)	
									

create table public.tbl_course_reg(co_id serial primary key ,
								co_name varchar(30) not null,
								co_date date not null,
								st_id integer not null,
								constraint st_id foreign key(st_id) references public.tbl_student(st_id)
								)
create table public.tbl_class(cls_id serial primary key ,
							cla_name varchar(30) not null,
							st_id integer not null,  /*FK*/
							co_id integer not null,
							teacher_id integer not null,
							room_id integer not null,
							cls_date date not null,
							cls_start_time time not null,
							cls_end_time time,
							constraint student_id foreign key(st_id)references public.tbl_student(st_id),
							constraint course_id foreign key(co_id)references public.tbl_course_reg(co_id),
							constraint teacher_id foreign key(teacher_id)references public.tbl_teacher(teacher_id),
							constraint room_id foreign key(room_id)references public.tbl_rooms(room_id)
							)
create table public.tbl_teacher(teacher_id serial primary key,
							 te_name varchar(40) not null,
							te_phone_No integer not null,
							te_email varchar(34)unique,
							te_gender varchar(20)not null,
							te_join_date date not null)	

create table public.tbl_rooms(room_id serial primary key,
							 roll_no integer unique)
							
create table public.tbl_quezies(quz_id serial primary key,
							quz_date date not null,
							quz_type_id integer not null,
							st_id integer not null,
							teacher_id integer not null,
							course_id integer not null,
							marks integer not null,
							
							constraint strudent_id foreign key(st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
						    constraint course_Id foreign key (course_id) references public.tbl_course_reg(co_id),
							constraint quz_type_id foreign key(quz_type_id) references public.tbl_quze_type(quz_type_id)
							
							
							)	
							
create table public.tbl_quze_type(quz_type_id serial primary key,
								quz_type_name varchar(10)not null)
								
create table public.tbl_paper(p_id serial primary key,
							st_id integer not null,
							teacher_id integer not null,
							quz_id integer not null,
							co_id integer not null,
							p_date date not null,
							total_marks integer not null,
							obtain_marks integer not null,
							
							
							constraint student_id foreign key (st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
							constraint quze_id foreign key (quz_id)references public.tbl_quezies(quz_id),
							constraint co_id foreign key (co_id)references public.tbl_course_reg(co_id)
							
							)	
							/* student free detilas */
							
							
create table public.tb_free(f_id serial primary key,
							   st_id integer not null,
							 f_date date not null,
							  invoce_no integer not null,
							
							last_date date not null,
							amount decimal(18,3) not null,
							free_dues_id integer not null,
								free_type_id integer not null,
								bank_id integer not null,
								
								constraint free_dues_id foreign key(free_dues_id) references public.tbl_free_dues(free_dues_id),
								constraint free_type_id foreign key(free_type_id) references public.tbl_free_type(free_type_id),
								constraint bank_id foreign key(bank_id) references public.tbl_bank(bank_id)
							
							)
create table public.tbl_free_dues(free_dues_id serial primary key,
								
								due_date date not null,
								due_amount decimal(18,3)not null)
create table public.tbl_free_type(free_type_id serial primary key,
								 free_type_name varchar(29),
								 status varchar(20) not null,
								  amount decimal(18,3) not null)
								
							
create table public.tbl_bank(bank_id serial primary key,
							 bank_name varchar(12) not null,
							bank_phone_no integer not null,
							schoo_account_no integer not null,
							deposit_date date not null,
							deposit_amount decimal(18,3)
							)	
							
							/* manage school employee*/
							
create table public.tbl_employee (emp_id serial primary key,
								  emp_name varchar(15) not null,
								   emp_NO integer not null,
								 emp_father_name varchar(12) not null,
								 emp_cnic_NO varchar(15) unique ,
								 emp_phoneN0 integer  unique,
								emp_join_date date not null,
								emp_status varchar(13) not null,
								emp_designation_id integer not null,
								emp_type_id integer not null,
								emp_category_id integer not null,
								
								constraint dsignation_id foreign key (emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint emp_type_id foreign key (emp_type_id) references public.tbl_employee_type(emp_type_id),
								constraint emp_category_id foreign key (emp_category_id) references public.tbl_employee_category(emp_category_id)
								)
create table public.tbl_designation (emp_designation_id serial primary key,
										 des_name varchar(19) not null)
create table public.tbl_employee_type(emp_type_id serial primary key,
										 emp_type_name varchar(14)not null)
create table public.tbl_employee_category(emp_category_id serial primary key,
											emp_cate_name varchar(14) not null)
											
											/* employee Salary manage database */
											
create table public.tbl_salary(salary_id serial primary key,
								 emp_id integer not null,
								 emp_designation_id integer not null,
								allwoance_id integer not null,
								bonus_is integer not null,
								advance_salary_id integer not null,
								total_salary decimal(18,3) not null,
								salary_ststus varchar(13),
								constraint employee_id foreign key(emp_id) references public.tbl_employee(emp_id),
								constraint designation_id foreign key(emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint allwoance_id foreign key(allwoance_id) references public.tbl_allawoance(allwoance_id),
								constraint bonus_id foreign key(bonus_is) references public.tbl_bonus(bonus_is),
								constraint advance_salary_id foreign key(advance_salary_id) references public.tbl_advance_salary(advance_salary_id)
								)
create table public.tbl_allawoance(allwoance_id serial primary key,
								all_name varchar(12) not null,
								all_status varchar(13) not null,
								all_amount decimal(18,3) not null)
								
create table public.tbl_bonus(bonus_is serial primary key,
							  bonus_name varchar(23) not null,
							  bonus_amount decimal(18,3) not null,
							bonus_status varchar(23) not null
							)		
							
create table public.tbl_advance_salary(advance_salary_id serial primary key,
									  emp_id integer not null,
									 advances_salary_for_months decimal(18,3) not null,
									 total_amount decimal(18,3) not null,
									recover_duration integer not null,
									per_month_recover_amount decimal(18,3) not null,
									recover_date date not null)
									
									
									/* user and role */
									
									
create table public.tbl_user (user_id serial primary key,
								 user_name varchar(39) not null,
								 password varchar(23) not null,
								role_id integer not null,
								constraint role_id foreign key(role_id) references public.tbl_role(role_id)
								)
create table public.tbl_role(role_id serial primary key,
							 role_name varchar(34) not null)								
								
								
								
							
									
									
									
									
									
									
									
									
									
									
									
									
/*Complete School Management system Database*/

create table public.tbl_Schoo(sch_id serial primary key,
							sch_name varchar(40) not null,
							sch_address varchar(50)not null,
							sch_phone_no integer unique)
							
create table public.tbl_student(st_id serial primary key,
							   roll_no integer unique,
							st_name varchar(40)not null,
							pa_id integer not null ,    /*FK*/
								reg_id integer not null, /*FK*/
							st_phone_no integer unique,
							st_DOB date not null,
							st_gender varchar(10)not null,
							st_email varchar(40)unique,
								constraint parient_id foreign key(pa_id) references tbl_parient(pa_id),
								constraint registration_id foreign key(reg_id) references public.tbl_registration(reg_id)
							)	
create table public.tbl_parient(pa_id serial primary key,
							 pa_name varchar(40)not null,
							pa_phone_no integer unique,
							Pa_occupation varchar(30)not null
							)	
create table public.tbl_registration(reg_id serial primary key,
									 reg_no integer not null,
									reg_date date not null)	
									

create table public.tbl_course_reg(co_id serial primary key ,
								co_name varchar(30) not null,
								co_date date not null,
								st_id integer not null,
								constraint st_id foreign key(st_id) references public.tbl_student(st_id)
								)
create table public.tbl_class(cls_id serial primary key ,
							cla_name varchar(30) not null,
							st_id integer not null,  /*FK*/
							co_id integer not null,
							teacher_id integer not null,
							room_id integer not null,
							cls_date date not null,
							cls_start_time time not null,
							cls_end_time time,
							constraint student_id foreign key(st_id)references public.tbl_student(st_id),
							constraint course_id foreign key(co_id)references public.tbl_course_reg(co_id),
							constraint teacher_id foreign key(teacher_id)references public.tbl_teacher(teacher_id),
							constraint room_id foreign key(room_id)references public.tbl_rooms(room_id)
							)
create table public.tbl_teacher(teacher_id serial primary key,
							 te_name varchar(40) not null,
							te_phone_No integer not null,
							te_email varchar(34)unique,
							te_gender varchar(20)not null,
							te_join_date date not null)	

create table public.tbl_rooms(room_id serial primary key,
							 roll_no integer unique)
							
create table public.tbl_quezies(quz_id serial primary key,
							quz_date date not null,
							quz_type_id integer not null,
							st_id integer not null,
							teacher_id integer not null,
							course_id integer not null,
							marks integer not null,
							
							constraint strudent_id foreign key(st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
						    constraint course_Id foreign key (course_id) references public.tbl_course_reg(co_id),
							constraint quz_type_id foreign key(quz_type_id) references public.tbl_quze_type(quz_type_id)
							
							
							)	
							
create table public.tbl_quze_type(quz_type_id serial primary key,
								quz_type_name varchar(10)not null)
								
create table public.tbl_paper(p_id serial primary key,
							st_id integer not null,
							teacher_id integer not null,
							quz_id integer not null,
							co_id integer not null,
							p_date date not null,
							total_marks integer not null,
							obtain_marks integer not null,
							
							
							constraint student_id foreign key (st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
							constraint quze_id foreign key (quz_id)references public.tbl_quezies(quz_id),
							constraint co_id foreign key (co_id)references public.tbl_course_reg(co_id)
							
							)	
							/* student free detilas */
							
							
	create table public.tb_free(f_id serial primary key,
							   st_id integer not null,
							 f_date date not null,
							  invoce_no integer not null,
							
							last_date date not null,
							amount decimal(18,3) not null,
							free_dues_id integer not null,
								free_type_id integer not null,
								bank_id integer not null,
								
								constraint free_dues_id foreign key(free_dues_id) references public.tbl_free_dues(free_dues_id),
								constraint free_type_id foreign key(free_type_id) references public.tbl_free_type(free_type_id),
								constraint bank_id foreign key(bank_id) references public.tbl_bank(bank_id)
							
							)
create table public.tbl_free_dues(free_dues_id serial primary key,
								
								due_date date not null,
								due_amount decimal(18,3)not null)
create table public.tbl_free_type(free_type_id serial primary key,
								 free_type_name varchar(29),
								 status varchar(20) not null,
								  amount decimal(18,3) not null)
								
							
create table public.tbl_bank(bank_id serial primary key,
							 bank_name varchar(12) not null,
							bank_phone_no integer not null,
							schoo_account_no integer not null,
							deposit_date date not null,
							deposit_amount decimal(18,3)
							)	
							
							/* manage school employee*/
							
create table public.tbl_employee (emp_id serial primary key,
								  emp_name varchar(15) not null,
								   emp_NO integer not null,
								 emp_father_name varchar(12) not null,
								 emp_cnic_NO varchar(15) unique ,
								 emp_phoneN0 integer  unique,
								emp_join_date date not null,
								emp_status varchar(13) not null,
								emp_designation_id integer not null,
								emp_type_id integer not null,
								emp_category_id integer not null,
								
								constraint dsignation_id foreign key (emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint emp_type_id foreign key (emp_type_id) references public.tbl_employee_type(emp_type_id),
								constraint emp_category_id foreign key (emp_category_id) references public.tbl_employee_category(emp_category_id)
								)
	create table public.tbl_designation (emp_designation_id serial primary key,
										 des_name varchar(19) not null)
	create table public.tbl_employee_type(emp_type_id serial primary key,
										 emp_type_name varchar(14)not null)
	create table public.tbl_employee_category(emp_category_id serial primary key,
											emp_cate_name varchar(14) not null)
											
											/* employee Salary manage database */
											
	create table public.tbl_salary(salary_id serial primary key,
								 emp_id integer not null,
								 emp_designation_id integer not null,
								allwoance_id integer not null,
								bonus_is integer not null,
								advance_salary_id integer not null,
								total_salary decimal(18,3) not null,
								salary_ststus varchar(13),
								constraint employee_id foreign key(emp_id) references public.tbl_employee(emp_id),
								constraint designation_id foreign key(emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint allwoance_id foreign key(allwoance_id) references public.tbl_allawoance(allwoance_id),
								constraint bonus_id foreign key(bonus_is) references public.tbl_bonus(bonus_is),
								constraint advance_salary_id foreign key(advance_salary_id) references public.tbl_advance_salary(advance_salary_id)
								)
create table public.tbl_allawoance(allwoance_id serial primary key,
								all_name varchar(12) not null,
								all_status varchar(13) not null,
								all_amount decimal(18,3) not null)
								
create table public.tbl_bonus(bonus_is serial primary key,
							  bonus_name varchar(23) not null,
							  bonus_amount decimal(18,3) not null,
							bonus_status varchar(23) not null
							)		
							
create table public.tbl_advance_salary(advance_salary_id serial primary key,
									  emp_id integer not null,
									 advances_salary_for_months decimal(18,3) not null,
									 total_amount decimal(18,3) not null,
									recover_duration integer not null,
									per_month_recover_amount decimal(18,3) not null,
									recover_date date not null)
									
									
									/* user and role */
									
									
	create table public.tbl_user (user_id serial primary key,
								 user_name varchar(39) not null,
								 password varchar(23) not null,
								role_id integer not null,
								constraint role_id foreign key(role_id) references public.tbl_role(role_id)
								)
create table public.tbl_role(role_id serial primary key,
							 role_name varchar(34) not null)								
								
								
								
							
									
									
									
									
									
									
									
									
									
									
									
									
/*Complete School Management system Database*/

create table public.tbl_Schoo(sch_id serial primary key,
							sch_name varchar(40) not null,
							sch_address varchar(50)not null,
							sch_phone_no integer unique)
							
create table public.tbl_student(st_id serial primary key,
							   roll_no integer unique,
							st_name varchar(40)not null,
							pa_id integer not null ,    /*FK*/
								reg_id integer not null, /*FK*/
							st_phone_no integer unique,
							st_DOB date not null,
							st_gender varchar(10)not null,
							st_email varchar(40)unique,
								constraint parient_id foreign key(pa_id) references tbl_parient(pa_id),
								constraint registration_id foreign key(reg_id) references public.tbl_registration(reg_id)
							)	
create table public.tbl_parient(pa_id serial primary key,
							 pa_name varchar(40)not null,
							pa_phone_no integer unique,
							Pa_occupation varchar(30)not null
							)	
create table public.tbl_registration(reg_id serial primary key,
									 reg_no integer not null,
									reg_date date not null)	
									

create table public.tbl_course_reg(co_id serial primary key ,
								co_name varchar(30) not null,
								co_date date not null,
								st_id integer not null,
								constraint st_id foreign key(st_id) references public.tbl_student(st_id)
								)
create table public.tbl_class(cls_id serial primary key ,
							cla_name varchar(30) not null,
							st_id integer not null,  /*FK*/
							co_id integer not null,
							teacher_id integer not null,
							room_id integer not null,
							cls_date date not null,
							cls_start_time time not null,
							cls_end_time time,
							constraint student_id foreign key(st_id)references public.tbl_student(st_id),
							constraint course_id foreign key(co_id)references public.tbl_course_reg(co_id),
							constraint teacher_id foreign key(teacher_id)references public.tbl_teacher(teacher_id),
							constraint room_id foreign key(room_id)references public.tbl_rooms(room_id)
							)
create table public.tbl_teacher(teacher_id serial primary key,
							 te_name varchar(40) not null,
							te_phone_No integer not null,
							te_email varchar(34)unique,
							te_gender varchar(20)not null,
							te_join_date date not null)	

create table public.tbl_rooms(room_id serial primary key,
							 roll_no integer unique)
							
create table public.tbl_quezies(quz_id serial primary key,
							quz_date date not null,
							quz_type_id integer not null,
							st_id integer not null,
							teacher_id integer not null,
							course_id integer not null,
							marks integer not null,
							
							constraint strudent_id foreign key(st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
						    constraint course_Id foreign key (course_id) references public.tbl_course_reg(co_id),
							constraint quz_type_id foreign key(quz_type_id) references public.tbl_quze_type(quz_type_id)
							
							
							)	
							
create table public.tbl_quze_type(quz_type_id serial primary key,
								quz_type_name varchar(10)not null)
								
create table public.tbl_paper(p_id serial primary key,
							st_id integer not null,
							teacher_id integer not null,
							quz_id integer not null,
							co_id integer not null,
							p_date date not null,
							total_marks integer not null,
							obtain_marks integer not null,
							
							
							constraint student_id foreign key (st_id)references public.tbl_student(st_id),
							constraint teacher_id foreign key (teacher_id)references public.tbl_teacher(teacher_id),
							constraint quze_id foreign key (quz_id)references public.tbl_quezies(quz_id),
							constraint co_id foreign key (co_id)references public.tbl_course_reg(co_id)
							
							)	
							/* student free detilas */
							
							
	create table public.tb_free(f_id serial primary key,
							   st_id integer not null,
							 f_date date not null,
							  invoce_no integer not null,
							
							last_date date not null,
							amount decimal(18,3) not null,
							free_dues_id integer not null,
								free_type_id integer not null,
								bank_id integer not null,
								
								constraint free_dues_id foreign key(free_dues_id) references public.tbl_free_dues(free_dues_id),
								constraint free_type_id foreign key(free_type_id) references public.tbl_free_type(free_type_id),
								constraint bank_id foreign key(bank_id) references public.tbl_bank(bank_id)
							
							)
create table public.tbl_free_dues(free_dues_id serial primary key,
								
								due_date date not null,
								due_amount decimal(18,3)not null)
create table public.tbl_free_type(free_type_id serial primary key,
								 free_type_name varchar(29),
								 status varchar(20) not null,
								  amount decimal(18,3) not null)
								
							
create table public.tbl_bank(bank_id serial primary key,
							 bank_name varchar(12) not null,
							bank_phone_no integer not null,
							schoo_account_no integer not null,
							deposit_date date not null,
							deposit_amount decimal(18,3)
							)	
							
							/* manage school employee*/
							
create table public.tbl_employee (emp_id serial primary key,
								  emp_name varchar(15) not null,
								   emp_NO integer not null,
								 emp_father_name varchar(12) not null,
								 emp_cnic_NO varchar(15) unique ,
								 emp_phoneN0 integer  unique,
								emp_join_date date not null,
								emp_status varchar(13) not null,
								emp_designation_id integer not null,
								emp_type_id integer not null,
								emp_category_id integer not null,
								
								constraint dsignation_id foreign key (emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint emp_type_id foreign key (emp_type_id) references public.tbl_employee_type(emp_type_id),
								constraint emp_category_id foreign key (emp_category_id) references public.tbl_employee_category(emp_category_id)
								)
	create table public.tbl_designation (emp_designation_id serial primary key,
										 des_name varchar(19) not null)
	create table public.tbl_employee_type(emp_type_id serial primary key,
										 emp_type_name varchar(14)not null)
	create table public.tbl_employee_category(emp_category_id serial primary key,
											emp_cate_name varchar(14) not null)
											
											/* employee Salary manage database */
											
	create table public.tbl_salary(salary_id serial primary key,
								 emp_id integer not null,
								 emp_designation_id integer not null,
								allwoance_id integer not null,
								bonus_is integer not null,
								advance_salary_id integer not null,
								total_salary decimal(18,3) not null,
								salary_ststus varchar(13),
								constraint employee_id foreign key(emp_id) references public.tbl_employee(emp_id),
								constraint designation_id foreign key(emp_designation_id) references public.tbl_designation(emp_designation_id),
								constraint allwoance_id foreign key(allwoance_id) references public.tbl_allawoance(allwoance_id),
								constraint bonus_id foreign key(bonus_is) references public.tbl_bonus(bonus_is),
								constraint advance_salary_id foreign key(advance_salary_id) references public.tbl_advance_salary(advance_salary_id)
								)
create table public.tbl_allawoance(allwoance_id serial primary key,
								all_name varchar(12) not null,
								all_status varchar(13) not null,
								all_amount decimal(18,3) not null)
								
create table public.tbl_bonus(bonus_is serial primary key,
							  bonus_name varchar(23) not null,
							  bonus_amount decimal(18,3) not null,
							bonus_status varchar(23) not null
							)		
							
create table public.tbl_advance_salary(advance_salary_id serial primary key,
									  emp_id integer not null,
									 advances_salary_for_months decimal(18,3) not null,
									 total_amount decimal(18,3) not null,
									recover_duration integer not null,
									per_month_recover_amount decimal(18,3) not null,
									recover_date date not null)
									
									
									/* user and role */
									
									
	create table public.tbl_user (user_id serial primary key,
								 user_name varchar(39) not null,
								 password varchar(23) not null,
								role_id integer not null,
								constraint role_id foreign key(role_id) references public.tbl_role(role_id)
								)
create table public.tbl_role(role_id serial primary key,
							 role_name varchar(34) not null)								
								
								
								
							
									
									
									
									
									
									
									
									
									
									
									
									