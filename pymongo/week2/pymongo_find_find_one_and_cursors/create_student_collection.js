
use school
var types = ['exam', 'homework', 'quiz']
for (student_id = 0; student_id < 100; student_id++) {
    for (type=0; type < 3; type++) {
	var r = {'student_id':student_id, 'type':types[type], 'score':Math.random() * 100};
	db.scores.insert(r)
    }
}
