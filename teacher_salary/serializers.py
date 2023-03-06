class SalarySerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

    class Meta:
        model = Salary
        fields = ['id', 'teacher', 'hourly_rate', 'hours_worked', 'total_salary']
        read_only_fields = ['hours_worked', 'total_salary']