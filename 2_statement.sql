/*
	create table assessments ( 
		date dateTime,
		username varchar(128),
		score float
	);
	
	Question :
	1) Provide a mysql select statement to return the following resultset structure:
			day; num_pos_scores; num_neg_scores
			Where ​num_pos_scores​ and ​num_neg_scores​ are the total number of positive score rows, and negative score rows in the table, for individual days between March 1st, 2011 and April 30th, 2011, both days inclusive.
	2) Provide a mysql select statement that returns all the days between January 1st, 2011 and June 30th, 2011, both days inclusive, where there were no negative scores.
*/

/* Answer : */

/* 1. */
	select
		ass_outer.date,
		(
			select coalesce(sum(score),0)
			from  assessments ass_inner
			where DATE_FORMAT(ass_inner.date,'%Y-%m-%d') = DATE_FORMAT(ass_outer.date,'%Y-%m-%d')
			and ass_inner.score > 0
		) as num_pos_scores,
		(
			select coalesce(sum(score),0)
			from assessments ass_inner
			where DATE_FORMAT(ass_inner.date,'%Y-%m-%d') = DATE_FORMAT(ass_outer.date,'%Y-%m-%d')
			and ass_inner.score < 0
		) as num_neg_scores
	from assessments ass_outer
	where ass_outer.date between "2011-03-01" and "2011-04-30"
	group by DATE_FORMAT(date,'%Y-%m-%d');
	
/* 2. */
	select * from assessments where date between '2011-01-01' and '2011-06-30' and score > 0 order by date asc;
